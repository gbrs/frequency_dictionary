import collections

with open('byte-of-python.txt') as f:
    txt = f.read(100000).lower().strip()
    for symbol in '0123456789.,:;-_()!@#$%^&*{}[]|\\/<>?=':
        txt = txt.replace(symbol, '')
    word_list = txt.split()
    for symbol in 'qwertyuopsdfghjklzxcvbnm':
        txt = txt.replace(symbol, '')
    # print(word_list)

freq_dict = collections.Counter(word_list)

# freq_dict = {}
# for word in word_list:
#     freq_dict[word] = freq_dict.setdefault(word, 0) + 1
# print(sorted(freq_dict.items(), key=lambda item: (-item[1], item[0])))

print(freq_dict.most_common()[10:100])
