"""______Списковые, словарные сборки_____"""

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
#####_____________________Task_1__________________
# first_result_all = [len(i) for i in first_strings]
first_result = [len(i) for i in first_strings if len(i) >= 5]
# print(first_result_all) # [4, 4, 10, 8, 8]
print(first_result)     # [10, 8, 8]
#####_____________________Task_2__________________
second_result = [(i, k) for i in first_strings for k in second_strings if len(i) == len(k)]
print(second_result)  # [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'),
                      # ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]

#####_____________________Task_3__________________
# third_result_all = {i: len(i) for i in (first_strings + second_strings)}
third_result = {i: len(i) for i in (first_strings + second_strings) if len(i) % 2 == 0}

# print(third_result_all)  ## {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8,
                          # 'Variable': 8, 'Task': 4, 'Git': 3, 'Comprehension': 13,
                          # 'Java': 4, 'Computer': 8, 'Assembler': 9}______________
print(third_result)       # {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8,
                          # 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}