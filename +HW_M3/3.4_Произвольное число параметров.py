'''                                 Задача "Однокоренные":
Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат
root_word или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве
результата своей работы.

                                         Пункты задачи:
Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
Создайте внутри функции пустой список same_words, который пополнится нужными словами.
При помощи цикла for переберите предполагаемо подходящие слова.
'''

def single_root_words(root_word, *other_words):  #одно обязательное слово в параметр root_word, а далее
    # неограниченную последовательность в параметр *other_words
    same_words = []
    root_word_own = root_word.lower()
    # same_words = [i for i in other_words if i in root_word] # попытка через list complehesion,
    # но поскольку там переопределение переменных, то оставил идею
    for i in other_words:
        other_words_lower = i.lower()
        if other_words_lower in root_word_own or root_word_own in other_words_lower:
            same_words.append(i)
        else:
            continue
    return same_words

a = single_root_words('лес', 'лесник', 'лесник', 'лесотехнический', 'лесок', )
a1 = single_root_words('лесник', 'лесник', 'лесотехнический', 'лесок', )
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print('\t', a,'\n\n', a1,'\n\n\t', result1, '\n\n\t\t', result2) # :)




