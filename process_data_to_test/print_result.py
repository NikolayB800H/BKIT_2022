def print_result(some_func):
    def decorated(*args, **kwargs):
        ret = some_func(*args, **kwargs)
        print(some_func.__name__)
        if isinstance(ret, dict):
            for i in ret:
                print('{} = {}'.format(i, ret[i]))
        elif isinstance(ret, list):
            for i in ret:
                print(i)
        else:
            print(ret)
        return ret
    return decorated

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

def main():
    test_1()
    test_2()
    test_3()
    test_4()

if __name__ == "__main__":
    main()
