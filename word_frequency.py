import time
import os

start = time.time()

file_size = os.path.getsize('./KCC150_Korean_sentences_EUCKR.txt')
f= open('./KCC150_K01.txt','r',encoding='cp949',errors='ignore')
datas = f.read()
datas2 = datas.split()

count = {}

for word in datas2:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word in count:
    print('freq'+str(count[word]), word)

print("파일크기 : ",file_size )
print("걸린시간 : ",time.time() - start)
