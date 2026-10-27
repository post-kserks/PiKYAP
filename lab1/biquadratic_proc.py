"""
Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0.
Процедурная парадигма (функции, оператор def).

Пример запуска:
    python3 biquadratic_proc.py 1 -5 4
"""
import sys
import math


def parse_coef(coef_str):
    '''
    Пробует преобразовать строку в действительное число.

    Returns:
        float | None: коэффициент или None, если строка некорректна
    '''
    try:
        return float(coef_str)
    except ValueError:
        return None


def get_coef(index, prompt):
    '''
    Читает коэффициент из командной строки или вводит с клавиатуры.
    Некорректные значения игнорируются, ввод повторяется.

    Args:
        index (int): номер параметра в командной строке
        prompt (str): приглашение для ввода коэффициента

    Returns:
        float: коэффициент уравнения
    '''
    if index < len(sys.argv):
        coef = parse_coef(sys.argv[index])
        if coef is not None:
            return coef
        print('Некорректное значение в командной строке: "{}"'.format(sys.argv[index]))

    while True:
        coef = parse_coef(input(prompt + ' '))
        if coef is not None:
            return coef
        print('Некорректное значение, повторите ввод.')


def get_discriminant(a, b, c):
    '''
    Дискриминант квадратного уравнения A*t^2 + B*t + C = 0, где t = x^2.
    '''
    return b * b - 4 * a * c


def roots_from_square(t):
    '''
    Действительные корни уравнения x^2 = t.
    '''
    if t > 0.0:
        sq = math.sqrt(t)
        return [-sq, sq]
    if t == 0.0:
        return [0.0]
    return []


def get_roots(a, b, c):
    '''
    Вычисляет действительные корни биквадратного уравнения.

    Returns:
        list[float] | None: отсортированный список корней,
        None - если корнем является любое число
    '''
    if a == 0.0:
        # Вырожденный случай: B*x^2 + C = 0
        if b == 0.0:
            return None if c == 0.0 else []
        return roots_from_square(-c / b)

    d = get_discriminant(a, b, c)
    squares = []
    if d == 0.0:
        squares.append(-b / (2.0 * a))
    elif d > 0.0:
        sq_d = math.sqrt(d)
        squares.append((-b + sq_d) / (2.0 * a))
        squares.append((-b - sq_d) / (2.0 * a))

    roots = []
    for t in squares:
        roots.extend(roots_from_square(t))
    return sorted(roots)


def print_roots(roots):
    '''
    Выводит корни уравнения.
    '''
    if roots is None:
        print('Корнем является любое действительное число')
    elif len(roots) == 0:
        print('Нет действительных корней')
    elif len(roots) == 1:
        print('Один корень: {}'.format(roots[0]))
    else:
        print('Корней: {} -> {}'.format(len(roots), ', '.join(str(r) for r in roots)))


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    print('Уравнение: {}*x^4 + {}*x^2 + {} = 0'.format(a, b, c))
    if a != 0.0:
        print('Дискриминант D = {}'.format(get_discriminant(a, b, c)))
    print_roots(get_roots(a, b, c))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
