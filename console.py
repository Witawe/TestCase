from classes.institute import Institute
from addstudent import addstud
from addspec import addspec
from addgroup import addgroup
from addsubject import addsubject
from addexam import addexam
from addexampoint import addexampoint
import sys


def main(*args):
    inst = Institute()
    if len(args[0]) == 1:
        print('Ошибка: например - console.py add stud')
        quit()
    if len(args[0]) == 3:
        if args[0][1] == 'add' and args[0][2] == 'stud':
            addstud(inst)
        if args[0][1] == 'add'and args[0][2] == 'spec':
            addspec(inst)
        if args[0][1] == 'add'and args[0][2] == 'group':
            addgroup(inst)
        if args[0][1] == 'add'and args[0][2] == 'subj':
            addsubject(inst)
        if args[0][1] == 'add'and args[0][2] == 'exam':
            addexam(inst)
        if args[0][1] == 'add'and args[0][2] == 'exampoint':
            addexampoint(inst)

if __name__ == "__main__":
    main(sys.argv)