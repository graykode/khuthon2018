import tensorflow as tf
import numpy as np

TRAIN_FILENAME = 'train'
TRAIN_DATA_FILENAME = TRAIN_FILENAME + '.data'
TRAIN_VOCAB_FILENAME = TRAIN_FILENAME + '.vocab'


SEQUENCE_LENGTH = 50 # 문장을 짜르는 갯수
NUM_CLASS = 3

# 그래프 초기화
tf.reset_default_graph()

def save(filename, row, ans):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write('%s\t%s\t%s\t%s\t%2f\n' % (row[0], row[1], row[2], row[3], ans))

def get_raw_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = []
        for line in f.read().splitlines():
            data.append(line.split('\t'))
    return data

def checking(filename):
  with open(filename, 'r', encoding='utf-8') as f:
      data = [line.split('\t') for line in f.read().splitlines()]
      for d in data:
          if(len(d) != 4):
              print(d)
        
def test():
    with tf.Session() as sess:
        vocab = load_vocab(TRAIN_VOCAB_FILENAME)
        cnn = TextCNN(SEQUENCE_LENGTH, NUM_CLASS, len(vocab), 128, [3,4,5], 128)
        saver = tf.train.Saver()
        saver.restore(sess, './textcnn.ckpt')
        print('model restored')
        
        #eval = get_raw_text('evaluate.txt')
        
        
        #data = read_raw_text('khu')

        input_text = "정말 맛있어요!! 덕분에 식사 잘하고가네요^^"
        tokens = tokenize(input_text)
        print(input_text)
        print(tokens)

        # 입력한 문장을 토큰으로 분해 후 패딩을 채운다.
        sequence = [get_token_id(t, vocab) for t in tokens]
        x = []
        while len(sequence) > 0:
            seq_seg = sequence[:SEQUENCE_LENGTH]
            sequence = sequence[SEQUENCE_LENGTH:]

            padding = [1] * (SEQUENCE_LENGTH - len(seq_seg))
            seq_seg = seq_seg + padding
            x.append(seq_seg)

        feed_dict = {
            cnn.input: x,
            cnn.dropout_keep_prob: 1.0
        }
        predict = sess.run([cnn.predictions], feed_dict)
        result = np.mean(predict)
            #print("%4f %4f" % (ans[0],ans[1]))
            #save('output.txt',d, ans[0],ans[1])
        print(round(result) + 1)

              
if __name__ == '__main__':
    test()
    print('done')