"""
Задача "Матрица воплоти":
Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать
матрицу(вложенный список) размерами n строк и m столбцов, заполненную значениями value и возвращать
эту матрицу в качестве результата работы.
Пункты задачи:
Объявите функцию get_matrix и напишите в ней параметры n, m и value.
Создайте пустой список matrix внутри функции get_matrix.
Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
В первом цикле добавляйте пустой список в список matrix.
Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
Во втором цикле пополняйте ранее добавленный пустой список значениями value.
После всех циклов верните значение переменной matrix.
Выведите на экран(консоль) результат работы функции get_matrix.
"""
def get_matrix(n, m, value):
    print('Строчный вариант написания матрицы')
    matrix = []
    for i in range(n):
        matrix_1 = []
        matrix.append(matrix_1)
        for j in range(m):
            matrix_1.append(value)
    print(matrix,'\n')
    def upgrade1_draw_matrix(matrix):
        print('\n','Матричный вар-т написания матрицы')
        for k in matrix:
            print(k)
    upgrade1_draw_matrix(matrix)
    def upgrade2_draw_matrix(matrix):
        print('\n','Распакованный матричный вар-т написания матрицы')
        for k in matrix:
            print(*k)
    upgrade2_draw_matrix(matrix)
    return matrix

get_matrix(4, 4, 1)
get_matrix(10, 10, 10)
get_matrix(2, 2, 2)
