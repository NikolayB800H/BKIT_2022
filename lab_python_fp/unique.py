import random
import copy

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = False
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        self.used_elements = set() 
        self.iterator = iter(items)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                current = next(self.iterator)
            except StopIteration:
                raise StopIteration
            cur_cpy = copy.copy(current)
            if self.ignore_case:
                cur_cpy = cur_cpy.casefold()
            if cur_cpy not in self.used_elements:
                self.used_elements.add(cur_cpy)
                return current

def main():
    # будет последовательно возвращать только 1 и 2
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for i in Unique(data):
        print(i, end = " ")
    print()
    # будет последовательно возвращать только 1, 2 и 3
    data = gen_random(10, 1, 3)
    for i in Unique(data):
        print(i, end = " ")
    print()
    # будет последовательно возвращать только a, A, b, B
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data):
        print(i, end = " ")
    print()
    # будет последовательно возвращать только a, b
    for i in Unique(data, ignore_case = True):
        print(i, end = " ")
    print()

if __name__ == "__main__":
    main()
