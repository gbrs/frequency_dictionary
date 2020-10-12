'''
На основе какого-то текста создаем его частотный словарь
'''

'''
TODO
таблицу неправильных глаголов добавить, хотя заставит учить часто встречающиеся неправильные глаголы
'''

import collections

# создаем список из слов текста
with open('VanderPlas.txt', encoding='utf-8') as f:
    txt = f.read().lower().strip()
    for symbol in '0123456789.,:;-_+=()!@#$%^&*{}[]|\\/<>?=`“”•–?"\'':
        txt = txt.replace(symbol, ' ')
    txt_list = txt.split()
    # print(word_list)

# считываем список уже знакомых мне слов
with open('vocabulary my.txt', encoding='utf-8') as f:
    my_vocabulary = f.read().lower().strip().split()
    # print(my_vocabulary)

freq_dict = collections.Counter(txt_list)

#  удаляем из словаря отдельные буквы (названия переменных скорее всего)
#  и знакомые мне слова удаляем
for symbol in 'qwertyuopsdfghjklzxcvbnm':
    freq_dict.pop(symbol, 0)
for word in my_vocabulary:
    freq_dict.pop(word, 0)

# создаем сортированный список всех встречающихся в текстке слов
word_list = list(set(txt_list))
word_list.sort()
# print(word_list)

# print(freq_dict.most_common()[:100])


# словоформы с добавленными -s -es -ed -ing удаляем, добавляя в статистику основного слова.
# Как просто решить вопрос с use и using (они далеко друг от друга)? Желательно не зацепив us.
# Этот алгоритм к сожалению us и uses счиатет одним словом.
for i in range(len(word_list) - 10):
    for j in range(i + 10, i, -1):
        if        (word_list[j] == ''.join([word_list[i], 's'])
                or word_list[j] == ''.join([word_list[i], 'ing'])
                or word_list[j] == ''.join([word_list[i], 'ed'])
                or word_list[j] == ''.join([word_list[i], 'es'])):
            freq_dict[word_list[i]] += freq_dict[word_list[j]]
            freq_dict.pop(word_list[j], 0)

# print(freq_dict.most_common()[:30])

# выводим в файл наш словарь
with open('frequency dictionary.txt', 'w', encoding='utf-8') as f:
    for word in freq_dict.most_common():  # почему не работает без .most_common()
        f.writelines(''.join([word[0], ' ', str(word[1]), '\n']))
