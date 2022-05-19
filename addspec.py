from classes.institute import Specialization, Institute
import sys

class main():
    inst = Institute()
    #print("Введите название специализации")
    #print("Пример: Фундаментальная информатика и информационные технологии")
    if len(sys.argv) < 2:
        print('Ошибка: example - addspec.py ФИИТ')
        quit()
    name = sys.argv[1]
    inst.add_spec(Specialization(name))
    if (len(inst.specs)) == 1:
        if name != '':
            print(inst.specs[-1].name)
            print("Специализация успешно добавлена")
        else:
            raise Exception("Ошибка добавления специализации")
            print("Ошибка добавления специализации")
