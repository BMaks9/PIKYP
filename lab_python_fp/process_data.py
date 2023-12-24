import json
import sys
from cm_timer import cm_timer_1
from print_result import print_result
from unique import Unique
from gen_random import gen_random

path = "lab_python_fp/data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return [i for i in  Unique([i["job-name"].lower() for i in arg])]

@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python" , arg))


@print_result
def f4(arg):
    return ['{}, зарплата {} руб.'.format(i[0], i[1]) for i in list(zip(arg, gen_random(len(arg), 100000, 200000)))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
