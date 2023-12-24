# Итератор для удаления дубликатов
from gen_random import gen_random
class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        if self.ignore_case:
            self.items = iter(set(''.join(items).lower()))
        else:
            self.items = iter(set(items))
    def __next__(self):
        return next(self.items)

    def __iter__(self):
        return self

def main():
    data = gen_random(10, 1, 3)
    a = Unique(data)
    for i in a:
        print(i)


if __name__ == '__main__':
    main()