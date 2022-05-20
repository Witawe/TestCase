from classes.institute import *
import sys

def addspec(institute):
    inst = Institute()
    name = input("Введите название специализации: ")
    inst.add_spec(Specialization(name))
    if (len(inst.specs)) == 1:
        print(inst.get_spec(name))
        print("Специализация успешно добавлена")
    else:
        raise Exception("Ошибка добавления специализации")
