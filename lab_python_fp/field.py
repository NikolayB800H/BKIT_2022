def field(items, *args):
    size = len(args)
    assert size > 0
    ret = {}
    for item in items:
        skip = True
        for arg in args:
            if item.get(arg) is not None:
                ret[arg] = item[arg]
                skip = False
        if not skip:
            if size == 1:
                yield ret[args[0]]
            else:
                yield ret
        ret.clear()


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'name': 'Skip me', 'addition': 'please'},
        {'title': 'Стол', 'color': 'brown'}
    ]
    oneFieldGen = field(goods, 'title')
    print('===== one field  =====')
    for i in oneFieldGen:
        print(i)
    twoFieldsGen = field(goods, 'title', 'price')
    print('===== two fields =====')
    for i in twoFieldsGen:
        print(i)

if __name__ == "__main__":
    main()
