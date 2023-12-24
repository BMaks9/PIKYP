# Здесь должна быть реализация декоратора
def print_result(func):
    def inner(*args, **kwargs):
        print(func.__name__)
        if type(func(*args, **kwargs)) == list : 
            print('\n'.join(map(str, func(*args, **kwargs))))
            return func(*args, **kwargs)
        elif type(func(*args, **kwargs)) == dict : 
            for i, j in func(*args, **kwargs).items():
                print(i, j, sep = ' = ')
            return func(*args, **kwargs)
        else :  
            print(func(*args, **kwargs))
            return func(*args, **kwargs)
    return inner

# Здесь должна быть реализация декоратора

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()