# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
def field(items, *args):
    assert len(args) > 0
    for i in items:
        if len(args) == 1:
            if args[0] in i:
                yield i[args[0]]
            else: continue
        else:
            d = {}
            for j in args:
                if not(j in i):
                    continue
                d[j] = i[j]
            yield d
def main():
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    for i in field(goods, 'title'):
        print(i)
    for i in field(goods, 'title', 'price'):
        print(i)
        
if __name__ == '__main__':
    main()