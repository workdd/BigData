ko_sentence_short = input()
ko_sentence_long = input()

if (len(ko_sentence_short) > len(ko_sentence_long)):
    ko_sentence_short, ko_sentence_long = ko_sentence_long, ko_sentence_short


def syllable_calculate(short, long):
    frequency_count = {}
    short_sum = 0
    for word in short:
        if (word != ' '):
            short_sum += 1
            frequency_count[word] = 0

    for word in long:
        for compared_word in frequency_count:
            if (word == compared_word):
                frequency_count[compared_word] += 1

    frequency_sum = 0
    for word in frequency_count:
        frequency_sum += frequency_count[word]

    frequency = frequency_sum / short_sum

    return frequency


print("음절 유사도: ", syllable_calculate(ko_sentence_short, ko_sentence_long))


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


print("어절 유사도: ", word_calculate(ko_sentence_short, ko_sentence_long))
