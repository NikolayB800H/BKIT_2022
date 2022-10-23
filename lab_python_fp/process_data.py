import json
import sys
from cm_timer import cm_timer_1
from print_result import print_result
import random

path = 'lab_python_fp/data.json'

with open(path) as f:
    data = json.load(f)

@print_result
def f1(arg):
    return list(map(lambda x: x[1], dict(map(lambda y: (y.casefold(), y), list(map(lambda x: x.get('job-name'), arg)))).items()))

@print_result
def f2(arg):
    return list(filter(lambda x: x.casefold().find('программист') == 0, arg))

@print_result
def f3(arg):
    return list(map(lambda z: z + ' с опытом Python', arg))

@print_result
def f4(arg):
    return list(zip(arg, list(map(lambda w: 'зарплата {} руб.'.format(random.randint(100000, 200000)), arg))))

def main():
    with cm_timer_1():
        f4(f3(f2(f1(data))))

if __name__ == '__main__':
    main()
