"""
Задача "Вызов разом"
"""
'''____Chisto Vspomnit____
     dict_ = {}
     dict_["MAMA"] = 32
     dict_["PAPA"] = 42
     print(dict_) # {'MAMA': 32, 'PAPA': 42}'''


def apply_all_func(int_list: list, *functions):
    """ 1) int_list - список из чисел (int, float)
        2)*functions - неограниченное кол-во функций из интовых listов (которые применимы к спискам,
            состоящим из чисел)"""
    results = {}
    for fucn in functions:
        results[fucn.__name__] = fucn(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))         # {'max': 20, 'min': 6}
print(apply_all_func([6, 20, 15, 9], len, sum, sorted)) # {'len': 4, 'sum': 50,
                                                      # 'sorted': [6, 9, 15, 20]}





