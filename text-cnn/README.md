# Text-CNN
Text-CNN을 사용해서 2018년 쿠톤(경희대학교 해커톤)에서 강의평가 긍정/부정도를 모델링 및 평가한 프로젝트입니다.



## What is Text-CNN

사실 [이 블로그](https://www.slideshare.net/langley0/textcnn-sentiment)를 읽어보면 자세히 알 수 있습니다. 더불어 NLP를 처음 접하시는 분이면 [파이콘 발표자료](https://www.lucypark.kr/docs/2015-pyconkr/#39)를 읽어보시는 것도 추천드립니다. (발표자 분이 konlpy 라이브러리 개발자로 알고있습니다. ㄷㄷ...) Text-CNN의 핵심은 **단어의 의미는 해당 단어의 문맥이 담고 있다는 것**입니다. Text-CNN에 대한 논문은 [Yoon Kim 2014](http://emnlp2014.org/papers/pdf/EMNLP2014181.pdf)이 좋습니다.



# Simple 코드리뷰

[영화 리뷰 관련 깃허브](https://github.com/e9t/nsmc/)를 보며 한 줄씩 해석해보면서 리뷰해봤고, 제 데이터에 더 좋게 일부분 수정했습니다.

먼저 파일 구조는 `TextCNN.py` , `preprocessing.py`, `train.py`, `test.py`로 이어져있습니다.



## PreProcessing.py

제 데이터를 전처리 하기 위한 코드입니다. 저는 데이터의 features를 `대학교`, `교수이름`, `과목이름`, `평점`, `댓글` 로 설정을 했고, 학습의 영향을 미치는 features는 `평점`과 `댓글`입니다.  

- 데이터 파일은 반드시 UTF-8로 인코딩되어있어야합니다. 
- 저는 데이터 한문장의 tokenize를 거친 형태소들을 최대 100개까지 보고, 나머지는 1(NULL)로 패딩처리했습니다.

- train데이터와 test데이터를 랜덤하게 셔플하여 8:2로 나누었습니다.
- 별점 1,2점은 0으로 3,4,5점은 1로 라벨링했습니다.
- 자세한 코드리뷰는 주석을 참고하세요.



## TextCNN.py

텐서플로우에서 모델의 핵심을 이루는 코드입니다. 사진 등은 [블로그](https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/)를 참조했습니다.

모델 파라미터는 다음과 같습니다.

- sequence_length : 앞서 지정한 한 문장의 최대 형태소 수입니다. (저는 100으로 설정), 단 이 값이 너무 크게 들어가면 train하는데 시간이 너무 많이 소요되고 argment error를 뿜기도 합니다. 더불어 convolution 상태에서 filter_size 만큼 묶어서 계산하는데 비용이 너무 많이 듭니다.
- num_classes : 앞에서 설명한 라벨링 one-hot요소입니다. 1이면 긍정, 0이면 부정
- vocab_size : 고유한 형태소의 갯수입니다. 직접 넣어주는것이 아니라 데이터에 따라 달라집니다.
- embedding_size : 각 형태소에 따른 벡터차원입니다. 쉽게 설명하면 word2vec과 같은 기능을 합니다.
- num_filters : 바이어스에 해당하는 필터(커널)의 수입니다.



![](http://i.imgur.com/JN72JHW.png)

'wait','for','the','video','and','do','n't', 'rent', 'it'이 각각 형태소이고, 저 한 줄(세로)이 sequence_length 입니다. 그리고 가로 차원이 embedding_size 이 됩니다. 이 아래 GIF가 처음 입력으로 주어지고 몇 개의 문장이 들어올지 모르므로 텐서의 shape는 `[None, sequence_length, embedding_size]`입니다.

![](http://i.imgur.com/1Flo6TK.gif)

```python
W = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0), name='W')

# [None, sequence_length, embedding_size]
# https://stackoverflow.com/questions/34870614/what-does-tf-nn-embedding-lookup-function-do/48438325#48438325 참고
embedded_chars = tf.nn.embedding_lookup(W, input)
```

`embedding_lookup` 함수는 word2vec과 같은 NLP에 자주 사용되는 함수로 설명은 위 스택오버플로우 문서를 참고하세요.



다른 핵심으로 convolution입니다. 제 코드에서는 convolution의 filter_size가 각 3,4,5이고 이는 3-gram, 4-gram, 5-gram을 나타냅니다. 즉 위 GIF에서 몇개의 형태소씩 묶어서 관계도를 볼건지를 나타냅니다.

![](http://i.imgur.com/WlGbDJfm.png)

convolution은 width로 `embedding_size`, height로 `filter size`가 들어갑니다. 위 GIF의 이동하는 빨간색 줄이 convolution입니다.

```python
conv = tf.nn.conv2d(
    embedded_chars,
    W,
    # 모두 1로 배치 데이터 하나씩, n-gram x embedding_size
    # 즉 n개의 단어씩을 포함하면서 한칸씩 움직인다는 말
    strides=[1, 1, 1, 1],
    padding='VALID',
name='conv')
```

strides는 모두 1로 설정했는데, `[batch_size, input_height, input_width, input_channels]`에 따르면 한 문장씩, 한 형태소씩 움직인다는 뜻입니다.



다음은 풀링인데 `sequence_length - filter_size + 1`이 되는 이유는 convolution을 거친 이후 텐서의 차원수가 `[batch_size, sequence_length - filter_size + 1, 1, num_filters]`이 되기 때문입니다.

```python
pooled = tf.nn.max_pool(
    h,
    # sequence_length - filter_size + 1이 중요
    ksize=[1, sequence_length - filter_size + 1, 1, 1],
    strides=[1, 1, 1, 1],
    padding='VALID',
    name='pool')
pooled_outputs.append(pooled)
```

이런식으로 3-gram conv -> pooling, 4-gram conv -> pooling -> 5-gram cov -> pooling을 거처 fully-connected 레이어에서 로지스틱하게 one-hot 방식으로 분류가 되면 끝입니다.

```python
num_filters_total = num_filters * len(filter_sizes)
h_pool = tf.concat(pooled_outputs, 3)
# 풀 커넥트 레이어를 만들기 위해 1열로 핀다.
h_pool_flat = tf.reshape(h_pool, [-1, num_filters_total])
scores = tf.nn.xw_plus_b(h_drop, W, b, name='scores')
losses = tf.nn.softmax_cross_entropy_with_logits(logits=scores, labels=label)
loss = tf.reduce_mean(losses)
```



## train.py

train.py를 돌리기 위해서는 test와 train셋이 있어야합니다.

10000번 트레이닝을 하고 `batch = random.sample(input, 64)`이니 데이터수는 64개보다 많아야합니다.

각 배치는 64개의 문장을 랜덤하게 뽑는데  의미는 아래와 같습니다.

```python
# x_batch는 한문장의 형태소 배열
# y_batch는 한문장의 라벨 결과값
x_batch, y_batch = zip(*batch)
```

100번 주기마다 test에서 배치를 뽑고 이로 정확성을 검사합니다.

모델을 평가할때는 드롭아웃을 1로 해주어야합니다.

```python
if current_step % 100 == 0:
# 100의 배수마다 test에서 데이터를 뽑아 evaluate한다.
batch = random.sample(test_input, 64)
x_test, y_test = zip(*batch)
evaluate(x_test, y_test)
```

1000번 주기마다 모델을 checkpoint 형식으로 저장합니다.

```python
if current_step % 1000 == 0:
# 1000의 배수마다 모델 세이빙
save_path = saver.save(sess, './textcnn.ckpt')
print('model saved : %s' % save_path)
```

쥬피터 노트북이나 구글 colab에서는 `tf.reset_default_graph()`를 해주어야 메모리에 올라간 텐서 그래프가 초기화됩니다.



## test.py

입력받은 문자를 tokenize하고 `SEQUENCE_LENGTH `보다 긴 형태소는 버리고 짧은 거는 0으로 패딩처리합니다. `SEQUENCE_LENGTH` 는 전처리와 같은 수로 해주는게 좋습니다.

이를 다음과 같이 평가합니다.

```python
feed_dict = {
    cnn.input: x,
    cnn.dropout_keep_prob: 1.0
}
predict = sess.run([cnn.predictions], feed_dict)
result = np.mean(predict)
```



# Google Colab

구글 코랩에서 konlpy 라이브러리를 사용할때는 다음과 같이 실행한 후에 테스트합니다. [참고](https://zzsza.github.io/data/2018/08/30/google-colab/#konlpy-%EC%84%A4%EC%B9%98)

konlpy 자체가 java기반으로 되어 있어서 반드시 설치해야합니다.

```shell
!apt-get update
!apt-get install g++ openjdk-8-jdk 
!pip3 install konlpy
!pip3 install data
```

설치 후 잘되는지 테스트

```python
from konlpy.tag import Twitter

twitter = Twitter()
twitter.pos("테스트입니다.")
```



## 레퍼런스
- [Text-CNN1](https://www.slideshare.net/langley0/textcnn-sentiment)
- [Text-CNN2](https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/)
- [Yoon Kim 2014](http://emnlp2014.org/papers/pdf/EMNLP2014181.pdf)
- [Tensorflow with text-cnn](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)
- [영화 리뷰 관련 깃허브](https://github.com/e9t/nsmc/)
- [한국어 형태소 분석 오픈소스](http://konlpy.org/ko/latest/)
- [파이콘 발표자료](https://www.lucypark.kr/docs/2015-pyconkr/#39)
- [그냥 읽어볼만한 깃허브](https://github.com/hoho0443/classify_comment_emotion)
- [로지스틱 회귀를 사용한 한국어 감성 분류](https://github.com/carpedm20/reviewduk)
