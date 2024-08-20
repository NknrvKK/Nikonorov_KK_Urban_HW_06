"""
Задача "Найдёт везде":
"""

class WordsFinder():

    def __init__(self, *files_name):
        self.files_name = files_name

    def get_all_words(self):
        """ 1) создали пустой словарь
            2) каждый файл из списка файлов открываем через рид и создаем новый
               файл с lower() словами для каждого файла
        3) избавляемся от знаков препинания
        4) разделяем полученный текст на отдельные слова
        5) """
        all_words = {}
        """В словарь all_words: 
            ключ - название файла, 
            значение - список из слов этого файла."""

        for file_name in self.files_name:
            with open(file_name, "r", encoding="utf-8") as file:
                new_file = file.read().lower()
                for _ in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    new_file = new_file.replace(_, ' ')
                words = new_file.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        dict_find = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            for i, w in enumerate(words, start=1):
                if w == word.lower():
                    dict_find[file_name] = i
                    break
        return dict_find

    def count(self, word):
        all_words = self.get_all_words()
        dict_count = {}
        for file_name, words in all_words.items():
            dict_count[file_name] = words.count(word.lower())
        return dict_count


###_______________Пример выполняемого кода:___________________

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



































## Задача "Найдёт везде":
# class WordsFinder:
#     def __init__(self, *files_name):
#         self.file_names = files_name
#
#     def get_all_words(self):
#         all_words = {}
#         for file_name in self.file_names:
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 text = file.read().lower()
#                 for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
#                     text = text.replace(punct, '')
#                 words = text.split()
#                 all_words[file] = words
#         return all_words
#
#     def find(self, word):
#         all_words = self.get_all_words()
#         result = {}
#         for file_name, words in all_words.items():
#             for i, w in enumerate(words):
#                 if w == word:
#                     result[file_name] = i
#         return result
#
#     def count(self, word):
#         all_words = self.get_all_words()
#         result = {}
#         for file_name, words in all_words.items():
#             result[file_name] = words.count(word)
#         return result
#
#
# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())  # Все слова
# print(finder2.find('TEXT'))  # 3 слово по счёту
# print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

#___V2____
# class WordsFinder:
#     def __init__(self, *file_name):
#         self.file_names = [*file_name]
#         self.file_name = file_name
#
#     def get_all_words(self):
#         all_words = {}
#         words = []
#         str_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
#         for file_name in self.file_names:
#             with open(file_name, 'r', encoding='utf-8') as opener:
#                 for line in opener:
#                     line = line.lower()
#                     for p in str_punctuation:
#                         if p in line:
#                             line = line.replace(p, ' ')
#                     split_line = line.split(sep=' ')
#                     words.append(split_line)
#         sorted_list = [x for y in words for x in y]
#         all_words[self.file_name] = sorted_list
#         return all_words
#
#     def find(self, word):
#         dict_ = self.get_all_words()
#         list_ = []
#         for name, words in dict_.items():
#             for w in words:
#                 if word.lower() in w:
#                     index = words.index(w)
#                     list_.append(self.file_name)
#                     list_.append(index+1)
#                     break
#         return list_
#
#     def count(self, word):
#         dict_ = self.get_all_words()
#         list_ = []
#         count = 0
#         for name, words in dict_.items():
#             for w in words:
#                 if word.lower() in w:
#                     count += 1
#         list_.append(self.file_name)
#         list_.append(count)
#         return list_
#
#
# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())
# print(finder2.find('TEXT'))
# print(finder2.count('teXT'))


