import random


# Пример:
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    print('gen_random(5, 1, 3):', list(gen_random(5, 1, 3)))
    print('gen_random(10, -5, 5):', list(gen_random(10, -5, 5)))
