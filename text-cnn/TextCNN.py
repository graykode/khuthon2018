import tensorflow as tf

# 레퍼런스
# https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/
# https://github.com/ioatr/textcnn
# http://emnlp2014.org/papers/pdf/EMNLP2014181.pdf
# http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/

class TextCNN(object):
    # sequence_length는 내가 지정한 한 문장의 최대 글자 수, 난 100으로 지정(단, 너무 크게해서는 안됨.)
    # num_classes는 2(추천, 비추천)
    # vocab_size는 중복되지 않는 형태소의 갯수
    # embedding_size는 각 형태소에 대한 벡터의 차원
    # filter_sizes n-gram끼리 묶어주는 n
    # num_filters 필터(커널)의 갯수, 여기서는 보통 128로 지정
    def __init__(self, sequence_length, num_classes, vocab_size, embedding_size, filter_sizes, num_filters):
        input = tf.placeholder(tf.int32, [None, sequence_length], name='input')
        label = tf.placeholder(tf.float32, [None, num_classes], name='label')
        dropout_keep_prob = tf.placeholder(tf.float32, name='dropout_keep_prob')

        with tf.name_scope('embedding'):
            # W는 https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/ 에서 빨간 레이어에 해당.
            W = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0), name='W')

            # [None, sequence_length, embedding_size]
            # https://stackoverflow.com/questions/34870614/what-does-tf-nn-embedding-lookup-function-do/48438325#48438325 참고
            embedded_chars = tf.nn.embedding_lookup(W, input)

            # [None, sequence_length, embedding_size, 1]
            # conv2d 함수가 요구하는 조건을 만족시키기 위해 1차원 추가
            embedded_chars = tf.expand_dims(embedded_chars, -1)

        pooled_outputs = []
        for i, filter_size in enumerate(filter_sizes):
            # 필터 사이즈가 3,4,5 (n-gram)인 컨볼루션을 만듬.
            with tf.name_scope('conv-maxpool-%s' % filter_size):
                # n-gram만큼 embedding_size하게 1채널에서 128개의 필터의 컨볼루션
                filter_shape = [filter_size, embedding_size, 1, num_filters]
                W = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1), name='W')
                b = tf.Variable(tf.constant(0.1, shape=[num_filters]), name='b')
                conv = tf.nn.conv2d(
                    embedded_chars,
                    W,
                    # 모두 1로 배치 데이터 하나씩, n-gram x embedding_size
                    # 즉 n개의 단어씩을 포함하면서 한칸씩 움직인다는 말
                    strides=[1, 1, 1, 1],
                    padding='VALID',
                    name='conv')
                h = tf.nn.relu(tf.nn.bias_add(conv, b), name='relu')
                pooled = tf.nn.max_pool(
                    h,
                    # sequence_length - filter_size + 1이 중요
                    ksize=[1, sequence_length - filter_size + 1, 1, 1],
                    strides=[1, 1, 1, 1],
                    padding='VALID',
                    name='pool')
                pooled_outputs.append(pooled)

        num_filters_total = num_filters * len(filter_sizes)
        h_pool = tf.concat(pooled_outputs, 3)
        # 풀 커넥트 레이어를 만들기 위해 1열로 핀다.
        h_pool_flat = tf.reshape(h_pool, [-1, num_filters_total])

        # 드롭아웃은 train 0.5, test 1.0로 설정
        with tf.name_scope('dropout'):
            h_drop = tf.nn.dropout(h_pool_flat, dropout_keep_prob)

        # prediction
        with tf.name_scope('output'):
            W = tf.get_variable('W', shape=[num_filters_total, num_classes],
                                initializer=tf.contrib.layers.xavier_initializer())
            b = tf.Variable(tf.constant(0.1, shape=[num_classes]), name='b')

            # W*x+b
            scores = tf.nn.xw_plus_b(h_drop, W, b, name='scores')
            # predictions은 1에 대한 조건분포 확률
            predictions = tf.argmax(scores, 1, name='predictions')

        # 크로스 엔트로피 손실 함수
        with tf.name_scope('loss'):
            losses = tf.nn.softmax_cross_entropy_with_logits(logits=scores, labels=label)
            loss = tf.reduce_mean(losses)

        with tf.name_scope('accuracy'):
            correct_predictions = tf.equal(predictions, tf.argmax(label, 1))
            accuracy = tf.reduce_mean(tf.cast(correct_predictions, 'float'), name='accuracy')

        # variables
        self.input = input
        self.label = label
        self.dropout_keep_prob = dropout_keep_prob
        self.predictions = predictions
        self.loss = loss
        self.accuracy = accuracy