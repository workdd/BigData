ko_sentence_short = input()
ko_sentence_long = input()

if (len(ko_sentence_short) > len(ko_sentence_long)):
    ko_sentence_short, ko_sentence_long = ko_sentence_long, ko_sentence_short


def ngram(short, long, type):
    frequency_count_bi = {}
    frequency_count_tri = {}
    short = short.replace(" ", "")
    long = long.replace(" ", "")
    short_sum_bi = 0
    short_sum_tri = 0
    if type == 2 or type == 5:
        for idx in range(len(short)):
            if idx == 0:
                frequency_count_bi['$' + short[idx]] = 0
            else:
                frequency_count_bi[short[idx - 1] + short[idx]] = 0
            short_sum_bi += 1

        for idx in range(len(long)):
            for compared_word in frequency_count_bi:
                if idx == 0:
                    if long[idx] == compared_word[1] and compared_word[0] == '$':
                        frequency_count_bi[compared_word] += 1
                else:
                    if long[idx - 1] + long[idx] == compared_word:
                        frequency_count_bi[compared_word] += 1
    if type == 3 or type == 5:
        for idx in range(len(short)):
            if idx == 0:
                frequency_count_tri['$' + '$' + short[idx]] = 0
            elif idx == 1:
                frequency_count_tri['$' + short[idx - 1] + short[idx]] = 0
            else:
                frequency_count_tri[short[idx - 2] + short[idx - 1] + short[idx]] = 0
            short_sum_tri += 1
        for idx in range(len(long)):
            for compared_word in frequency_count_tri:
                if idx == 0:
                    if long[idx] == compared_word[2] and compared_word[0] == '$':
                        frequency_count_tri[compared_word] += 1
                elif idx == 1:
                    if long[idx - 1] + long[idx] == compared_word[1] + compared_word[2] and compared_word[0] == '$':
                        frequency_count_tri[compared_word] += 1
                else:
                    if long[idx - 2] + long[idx - 1] + long[idx] == compared_word:
                        frequency_count_tri[compared_word] += 1

    if type == 2:
        frequency_sum_bi = 0
        for word in frequency_count_bi:
            frequency_sum_bi += frequency_count_bi[word]
        frequency_bi = frequency_sum_bi / short_sum_bi
        return frequency_bi
    elif type == 3:
        frequency_sum_tri = 0
        for word in frequency_count_tri:
            frequency_sum_tri += frequency_count_tri[word]
        frequency_tri = frequency_sum_tri / short_sum_tri
        return frequency_tri
    elif type == 5:
        frequency_sum_bi = 0
        for word in frequency_count_bi:
            frequency_sum_bi += frequency_count_bi[word]
        frequency_bi = frequency_sum_bi / short_sum_bi
        frequency_sum_tri = 0
        for word in frequency_count_tri:
            frequency_sum_tri += frequency_count_tri[word]
        frequency_tri = frequency_sum_tri / short_sum_tri
        return frequency_tri / frequency_bi


print("bigram 음절 유사도: ", ngram(ko_sentence_short, ko_sentence_long, 2))
print("trigram 음절 유사도: ", ngram(ko_sentence_short, ko_sentence_long, 3))
print("bigram , trigram 음절 유사도: ", ngram(ko_sentence_short, ko_sentence_long, 5))
