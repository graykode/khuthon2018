import tensorflow as tf
import numpy as np
import preprocessing as pre
import TextCNN

TRAIN_FILENAME = 'train'
TRAIN_DATA_FILENAME = TRAIN_FILENAME + '.data'
TRAIN_VOCAB_FILENAME = TRAIN_FILENAME + '.vocab'

SEQUENCE_LENGTH = pre.SEQUENCE_LENGTH # 문장을 짜르는 갯수
NUM_CLASS = 2

# 그래프 초기화
tf.reset_default_graph()

def test():
    with tf.Session() as sess:
        vocab = pre.load_vocab(TRAIN_VOCAB_FILENAME)
        cnn = TextCNN(SEQUENCE_LENGTH, NUM_CLASS, len(vocab), 128, [3, 4, 5], 128)
        saver = tf.train.Saver()
        saver.restore(sess, './textcnn.ckpt')
        print('model restored')

        input_text = input('사용자 평가를 문장으로 입력하세요: ')
        tokens = pre.tokenize(input_text)
        print('입력 문장을 다음의 토큰으로 분해:')
        print(tokens)

        # 입력한 문장을 토큰으로 분해 후 패딩을 채운다.
        sequence = [pre.get_token_id(t, vocab) for t in tokens]
        x = []
        while len(sequence) > 0:
            seq_seg = sequence[:SEQUENCE_LENGTH]
            sequence = sequence[SEQUENCE_LENGTH:]

            padding = [1] * (SEQUENCE_LENGTH - len(seq_seg))
            seq_seg = seq_seg + padding
            print(seq_seg)
            x.append(seq_seg)

        feed_dict = {
            cnn.input: x,
            cnn.dropout_keep_prob: 1.0
        }
        predict = sess.run([cnn.predictions], feed_dict)
        result = np.mean(predict)
        print(result)
        if (result > 0.75):
            print('추천')
        elif (result < 0.25):
            print('비추천')
        else:
            print('평가 불가능')


if __name__ == '__main__':
    while True:
        tf.reset_default_graph()
        test()