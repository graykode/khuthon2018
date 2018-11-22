from konlpy.tag import Twitter
import random

pos_tagger = Twitter()
SEQUENCE_LENGTH = 60

type = ['Number', 'Punctuation']
prohibition = ['          ', ',', ')']

def tokenize(doc):
    result = []
    for t in pos_tagger.pos(doc, norm=True, stem=True):
        if t[1] not in type and t[0] not in prohibition:
            result.append('/'.join(t))
    return result

# 파일 데이터는 UTF-8 인코딩이어야함.
def read_raw_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]

        # data[1:]로 맨위 row를 뺀다
        # 3번 칼럼이 포인트, 4번이 댓글
        data = [(tokenize(row[4]), int(float(row[3]))) for row in data]
    return data

# 단순히 텍스트 파일 셔플링
def read_raw_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = [row for row in data[1:]]

        # 중요!! 반드시 셔플시켜야함.
        random.shuffle(data)
    return data

# 고유 형태소와 ID를 배치
def build_vocab(tokens):
    vocab = dict()
    vocab['#UNKOWN'] = 0
    vocab['#PAD'] = 1
    for t in tokens:
        if t not in vocab:
            vocab[t] = len(vocab)
    return vocab

# *.data 파일에 대해 짝수번은 데이터, 홀수번은 라벨링하여 배열로 가져옴
def load_data(filename):
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(int(len(lines) / 2)):
            data = lines[i * 2]
            label = lines[i * 2 + 1]
            result.append(([int(s) for s in data.split(',')], [int(s) for s in label.split(',')]))
    return result

# *.vocab 파일을 불러오는 함수
def load_vocab(filename):
    result = dict()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            ls = line.split('\t')
            result[ls[0]] = int(ls[1])
    return result

# 고유형태소에서 ID 가져오기
def get_token_id(token, vocab):
    if token in vocab:
        return vocab[token]
    else:
        return 0  # 형태소 맵에 들어있지 않을땐 0반환

# one-hot 방식으로 포인트 1,2는 0, 3,4,5는 1로 라벨링
def get_onehot(score):
    onehot = [0] * 2
    if score == 1 or score == 2:
        onehot[0] = 1
    elif score == 3 or score == 4 or score == 5:
        onehot[1] = 1
    return onehot

# *.data 파일 생성
def save_data(filename, data):
    def make_csv_str(d):
        output = '%d' % d[0]
        for index in d[1:]:
            output = '%s,%d' % (output, index)
        return output

    with open(filename, 'w', encoding='utf-8') as f:
        for d in data:
            data_str = make_csv_str(d[0])
            label_str = make_csv_str(d[1])
            f.write(data_str + '\n')
            f.write(label_str + '\n')

# *.vocab 파일 생성
def save_vocab(filename, vocab):
    with open(filename, 'w', encoding='utf-8') as f:
        for v in vocab:
            f.write('%s\t%d\n' % (v, vocab[v]))

# 단순히 배열을 텍스트 파일로 저장
def save_text(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        for d in data:
            f.write('%s\t%s\t%s\t%s\t%s\n' % (d[0], d[1], d[2], d[3], d[4]))

def build_input(data, vocab):

    result = []
    for d in data:
        ## d[0] NLP화된 댓글, d[1] 평점
        sequence = [get_token_id(t, vocab) for t in d[0]]
        ## 한 문장에 대해 n자까지 나머지는 1로 패딩을 채운다.
        while len(sequence) > 0:
            seq_seg = sequence[:SEQUENCE_LENGTH]
            sequence = sequence[SEQUENCE_LENGTH:]

            padding = [1] * (SEQUENCE_LENGTH - len(seq_seg))
            seq_seg = seq_seg + padding
            get_onehot(d[1])
            result.append((seq_seg, get_onehot(d[1])))

    return result
  
def check(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        for d in data:
            if(len(d) != 5):
                print(d)

if __name__ == '__main__':
    check('everytime')
    raw_data = read_raw_text('everytime')
    print('pos_tagger finish')

    rows = len(raw_data)
    bound = int(rows * 0.8)

    save_text('train', raw_data[:bound])
    save_text('test', raw_data[bound + 1:])