from konlpy.tag import Mecab
import os
import time

start = time.time()

f = open('./KCC150_Korean_sentences_EUCKR.txt', 'r', encoding='cp949', errors='ignore')
datas = f.readlines()
ko_sentence = input('한글 문장을 입력하세요: ')
n = int(input('추출문장 개수를 입력하세요: '))
m = Mecab()

splited_sentence = m.morphs(ko_sentence)


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

    frequency = frequency_sum / len(s)

    return frequency


big_count = {}
for data in datas:
    big_count[data] = 0
    big_count[data] += calculate(splited_sentence, m.morphs(data))
print("걸린시간 : ", time.time() - start)
big_count = sorted(big_count.items(), key=(lambda x: x[1]), reverse=True)

print(big_count[:n])
