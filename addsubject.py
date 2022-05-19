# from classes.institute import *
# import sys
#
# class main():
#     inst = Institute()
#     if len(sys.argv) < 2:
#         print('Ошибка: example - addspec.py Б1.О.07 Машинное обучение 2 288 spec')
#         quit()
#     name = sys.argv[1]
#     inst.add_spec(Specialization(name))
#     if (len(inst.specs)) == 1:
#         if name != '':
#             print(inst.specs[-1].name)
#             print("Специализация успешно добавлена")
#         else:
#             raise Exception("Ошибка добавления специализации")
#             print("Ошибка добавления специализации")