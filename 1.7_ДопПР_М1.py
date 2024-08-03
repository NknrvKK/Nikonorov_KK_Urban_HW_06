"""
Задание "Средний балл":

На вход даны следующие данные:
Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
Например: 'Aaron' - [5, 3, 3, 5, 4]
Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя
ученика, а значением - его средний балл.

Вывод в консоль:
{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

Примечания:
Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).
"""
def funcGr(a):
    G = round(sum(a) / len(a), 2)
    return(G)

# 1-й вар-т
# !!!___arg.sort() - просто как метод
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students_1 = students.sort() # Метод .sort - упорядочивает по алфавиту
print(students)
dict_ = {}
for i in range(len(grades)):
    dict_[students[i]] = funcGr(grades[i])
print(dict_, '\n', '\n') # {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.67, 'Steve': 4.8}


# 2-й вар-т
# !!!___sorted(arg) - как самостоятельная функция
grades1 = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students1 = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students1 = list(students1)
students_2 = sorted(students1) # Метод .sort - упорядочивает по алфавиту
print(students_2)
dict_ = {}
for i in range(len(grades1)):
    dict_[students_2[i]] = funcGr(grades1[i])
print(dict_) # {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.67, 'Steve': 4.8}