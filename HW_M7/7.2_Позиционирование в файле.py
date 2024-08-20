# # Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта.\
# Задача "Записать и запомнить":

###__V1_Без оператора with - через open(f_n,"w", encoding="")_____
###________________________--> f_n.close()________________________

def custom_write(file_name, strings):
    strings_positions = {}
    file_modified = open(file_name, 'a', encoding='utf-8')
    for num, string in enumerate(strings, start=1): # enumerate - состоит из 2 аргументов
        # - номера в списке (если не указан старт, то начинаем с 0) и самого эл-та из
        # списка под данным номером
        num_byte = file_modified.tell()
        file_modified.write(string + '\n')
        strings_positions[num, num_byte] = string
    file_modified.close()
    return strings_positions


###________________V2_С оператором with_______________________
# def custom_write(file_name, strings):
#     strings_positions = {}
#     with open(file_name, "w", encoding="utf-8") as f_mod:
#         for i, string in enumerate(strings, start=1):
#             num_byte = f_mod.tell()
#             f_mod.write(string + '\n')
#             strings_positions[i, num_byte] = string
#     return strings_positions


###_______________Пример выполняемого кода:___________________

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)