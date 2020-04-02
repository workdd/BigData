from konlpy.tag import Hannanum

hannanum = Hannanum()

ko_sentence_short = input()
ko_sentence_long = input()

hannanum.morphs(ko_sentence_short)
hannanum.morphs(ko_sentence_long)

def word_calculate(short, long):
    frequency_count = {}
    long_word_arr = long.split(" ")
    short_word_arr = short.split(" ")

    for word in short_word_arr:
        frequency_count[word] = 0


    for word in long_word_arr:
        for compared_word in frequency_count:
            if (word == compared_word):
                frequency_count[word] += 1

    frequency_sum = 0
    for word in frequency_count:
        frequency_sum += frequency_count[word]

    frequency = frequency_sum / len(short_word_arr)

    return frequency


print("형태소 유사도: ", word_calculate(ko_sentence_short, ko_sentence_long))
