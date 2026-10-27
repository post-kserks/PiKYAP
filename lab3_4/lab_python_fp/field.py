# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            result = {key: item[key] for key in args if item.get(key) is not None}
            if result:
                yield result


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': None, 'color': 'white'},
        {'title': 'Стелаж', 'price': 7000, 'color': None},
    ]
    print("field(goods, 'title'):")
    print(list(field(goods, 'title')))
    print("field(goods, 'title', 'price'):")
    print(list(field(goods, 'title', 'price')))
    print("field(goods, 'title', 'price', 'color'):")
    print(list(field(goods, 'title', 'price', 'color')))
