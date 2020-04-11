from konlpy.tag import Kkma, Okt, Komoran
import time

start = time.time()

mode = input('형태소 분석기를 선택하세요 - kkma:ka, okt:o, komoran: ko')
ko_sentence = input('한글 문장을 입력하세요: ')
n = int(input('추출문장 개수를 입력하세요: '))

f = open('./xaa', 'r', encoding='cp949', errors='ignore')
datas = f.readlines()

kkma = Kkma()
okt = Okt()
komoran = Komoran()


def morph(s):
    if mode == 'ka':
        return kkma.morphs(s)
    elif mode == 'o':
        return okt.morphs(s)
    elif mode == 'ko':
        return komoran.morphs(s)


splited_sentence = morph(ko_sentence)


def calculate(s, compared_s):
    freqency_count = {}

    for token in s:
        freqency_count[token] = 0

    for com_token in compared_s:
        for token in freqency_count:
            if com_token == token:
                freqency_count[token] += 1
    frequency_sum = 0
    for token in freqency_count:
        frequency_sum += freqency_count[token]

    frequency = frequency_sum / min(len(s), len(compared_s))

    return frequency


big_count = {}
for data in datas:
    big_count[data] = 0
    big_count[data] += calculate(splited_sentence, morph(data))
print("걸린시간 : ", time.time() - start)
big_count = sorted(big_count.items(), key=(lambda x: x[1]), reverse=True)

for data in big_count:
    if n <= 0:
        break
    print(data[0], data[1])
    n -= 1
