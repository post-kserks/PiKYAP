from gen_random import gen_random


# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # ignore_case = True - строки в разном регистре считаются одинаковыми
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()

    def _key(self, item):
        if self.ignore_case and isinstance(item, str):
            return item.lower()
        return item

    def __next__(self):
        # StopIteration исходного итератора завершает и этот итератор
        while True:
            item = next(self.items)
            key = self._key(item)
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print('Unique({}):'.format(data), list(Unique(data)))

    print('Unique(gen_random(10, 1, 3)):', list(Unique(gen_random(10, 1, 3))))

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('Unique({}):'.format(data), list(Unique(data)))
    print('Unique({}, ignore_case=True):'.format(data), list(Unique(data, ignore_case=True)))
