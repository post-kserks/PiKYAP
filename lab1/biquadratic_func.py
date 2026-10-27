"""
Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0.
Функциональная парадигма (сопоставление с образцом, match/case).
Требуется Python 3.10+.

Пример запуска:
    python3 biquadratic_func.py 1 -5 4
"""
import sys
import math
from itertools import chain

PROMPTS = ('Введите коэффициент А:', 'Введите коэффициент B:', 'Введите коэффициент C:')


def parse_coef(coef_str):
    try:
        return float(coef_str)
    except ValueError:
        return None


def input_coef(prompt):
    '''
    Рекурсивно запрашивает коэффициент, пока он не будет введён корректно.
    '''
    match parse_coef(input(prompt + ' ')):
        case float(coef):
            return coef
        case None:
            print('Некорректное значение, повторите ввод.')
            return input_coef(prompt)


def get_coef(arg, prompt):
    '''
    arg - значение из командной строки (или None, если оно не задано).
    '''
    match arg, parse_coef(arg) if arg is not None else None:
        case None, _:
            return input_coef(prompt)
        case _, float(coef):
            return coef
        case _, None:
            print('Некорректное значение в командной строке: "{}"'.format(arg))
            return input_coef(prompt)


def get_coefs(args):
    # Дополняем список аргументов значениями None до трёх элементов
    padded = (list(args) + [None, None, None])[:3]
    return tuple(map(get_coef, padded, PROMPTS))


def discriminant(a, b, c):
    return b * b - 4 * a * c


def roots_from_square(t):
    '''
    Действительные корни уравнения x^2 = t.
    '''
    match t:
        case 0.0:
            return (0.0,)
        case t if t > 0.0:
            return (-math.sqrt(t), math.sqrt(t))
        case _:
            return ()


def squares(a, b, c):
    '''
    Действительные корни относительно t = x^2,
    либо None, если корнем является любое число.
    '''
    match a, b, c:
        case 0.0, 0.0, 0.0:
            return None
        case 0.0, 0.0, _:
            return ()
        case 0.0, _, _:
            return (-c / b,)
        case _:
            match discriminant(a, b, c):
                case 0.0:
                    return (-b / (2.0 * a),)
                case d if d > 0.0:
                    return ((-b + math.sqrt(d)) / (2.0 * a), (-b - math.sqrt(d)) / (2.0 * a))
                case _:
                    return ()


def get_roots(a, b, c):
    '''
    Отсортированный кортеж действительных корней,
    либо None, если корнем является любое число.
    '''
    match squares(a, b, c):
        case None:
            return None
        case ts:
            return tuple(sorted(chain.from_iterable(map(roots_from_square, ts))))


def format_roots(roots):
    match roots:
        case None:
            return 'Корнем является любое действительное число'
        case ():
            return 'Нет действительных корней'
        case (x,):
            return 'Один корень: {}'.format(x)
        case _:
            return 'Корней: {} -> {}'.format(len(roots), ', '.join(map(str, roots)))


def main():
    a, b, c = get_coefs(sys.argv[1:])
    print('Уравнение: {}*x^4 + {}*x^2 + {} = 0'.format(a, b, c))
    if a != 0.0:
        print('Дискриминант D = {}'.format(discriminant(a, b, c)))
    print(format_roots(get_roots(a, b, c)))


if __name__ == "__main__":
    main()
