# # def calculate_structure_sum(args):
# #     sum = 0
# #     for i in args:
# #         if isinstance(i, list):
# #             sum += calculate_structure_sum(i)
# #         elif isinstance(i, tuple):
# #             sum += calculate_structure_sum(i)
# #         elif isinstance(i, set):
# #             sum += calculate_structure_sum(i)
# #         elif isinstance(i, dict):
# #             sum += calculate_structure_sum(i.keys())
# #             sum += calculate_structure_sum(i.values())
# #         elif isinstance(i, int):
# #             sum += i
# #         elif isinstance(i, str):
# #             sum += len(i)
# #     return sum
# #
# # data_structure = [
# #   [1, 2, 3],
# #   {'a': 4, 'b': 5},
# #   (6, {'cube': 7, 'drum': 8}),
# #   "Hello",
# #   ((), [{(2, 'Urban', ('Urban2', 35))}])
# # ]
# #
# # print(calculate_structure_sum(data_structure))
#
#
# # print({'a': 4, 'b': 5}.keys()) # dict_keys(['a', 'b'])
# # print({'a': 4, 'b': 5}.values()) # dict_values([4, 5])
#
#
#
#
#
# # print(t[3])
# #
# # print({'a': 4, 'b': 5}.items()) # dict_items([('a', 4), ('b', 5)])
#
#
#
# # Для кортежа
# def f1(t):
#     sum = 0
#     for i in t:
#         if isinstance(i, tuple):
#             sum += f1(i)
#         elif isinstance(i, int):
#             sum += i
#     return sum
# t = (1, 2, 3, 4, 5)
# print(f1(t))
#
#
# # Для словаря в списке
# def f1(t):
#     sum = 0
#     for i in t:
#         if isinstance(i, dict):
#             for k in i.items(): # получаем список из данных dict_items([('qaw', 123), ('ret', 0)])
#                 sum += f1(k)
#         elif isinstance(i, list):
#             sum += f1(i)
#         elif isinstance(i, set):
#             sum += f1(i)
#         elif isinstance(i, tuple):
#             sum += f1(i)
#         elif isinstance(i, str):
#             sum += len(i)
#         elif isinstance(i, int):
#             sum += i
#     return sum
d = {'qaw': 123, 'ret': 0 }
# print(f1(d))
#
#
# print(calculate_structure_sum(d))
print(d.items()) # dict_items([('qaw', 123), ('ret', 0)])
print(d.values()) # dict_values([123, 0])
print(d.keys()) # dict_keys(['qaw', 'ret'])
