from classes.institute import *
import sys

class main():
    inst = Institute()
    if len(sys.argv) > 8:
        print('Ошибка: example - addspec.py М-ФИИТ-21 2021 Фундаментальная информатика и информационные технологии')
        quit()
    name = sys.argv[1]
    year = sys.argv[2]
    spec = ''
    k = 0
    for i in sys.argv[3:8]:
        k = k + 1
        spec = spec + i
        if k <= 4:
            spec = spec + " "
    inst.add_group(Group(str(name), int(year), Specialization(spec)))
    if (len(inst.groups)) == 1:
        print(inst.groups[-1])
        print("Группа успешно добавлена")
    else:
        raise Exception("Ошибка добавления группы")
        print("Ошибка добавления группы")