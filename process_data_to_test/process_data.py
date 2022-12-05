import json
import sys
from process_data_to_test.print_result import print_result
import random

@print_result
def f1(arg):
    return list(map(lambda x: x[1], sorted(list(map(lambda y: (y.casefold(), y), list(map(lambda x: x.get('job-name'), arg)))))))

@print_result
def f2(arg):
    return list(filter(lambda x: x.casefold().find('программист') == 0, arg))

@print_result
def f3(arg):
    return list(map(lambda z: z + ' с опытом Python', arg))

@print_result
def f4(arg):
    return list(zip(arg, list(map(lambda w: 'зарплата {} руб.'.format(random.randint(100000, 200000)), arg))))
