"""
Решение биквадратного уравнения A*x^4 + B*x^2 + C = 0.
Объектно-ориентированная парадигма (классы).

Пример запуска:
    python3 biquadratic_oop.py 1 -5 4
"""
import sys
import math


class CoefReader:
    '''
    Чтение коэффициентов из командной строки или с клавиатуры.
    '''

    def __init__(self, args):
        self.args = args

    @staticmethod
    def parse(coef_str):
        try:
            return float(coef_str)
        except ValueError:
            return None

    def read(self, index, prompt):
        '''
        Возвращает корректный коэффициент: из параметра командной строки
        с номером index, иначе - введённый с клавиатуры.
        '''
        if index < len(self.args):
            coef = self.parse(self.args[index])
            if coef is not None:
                return coef
            print('Некорректное значение в командной строке: "{}"'.format(self.args[index]))

        while True:
            coef = self.parse(input(prompt + ' '))
            if coef is not None:
                return coef
            print('Некорректное значение, повторите ввод.')


class BiquadraticEquation:
    '''
    Биквадратное уравнение A*x^4 + B*x^2 + C = 0.
    '''

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return '{}*x^4 + {}*x^2 + {} = 0'.format(self.a, self.b, self.c)

    @property
    def discriminant(self):
        '''
        Дискриминант уравнения A*t^2 + B*t + C = 0, где t = x^2.
        '''
        return self.b * self.b - 4 * self.a * self.c

    @property
    def is_identity(self):
        '''
        True, если корнем является любое число.
        '''
        return self.a == 0.0 and self.b == 0.0 and self.c == 0.0

    @staticmethod
    def _roots_from_square(t):
        if t > 0.0:
            sq = math.sqrt(t)
            return [-sq, sq]
        if t == 0.0:
            return [0.0]
        return []

    def _squares(self):
        '''
        Действительные корни относительно t = x^2.
        '''
        a, b, c = self.a, self.b, self.c
        if a == 0.0:
            # Вырожденный случай: B*x^2 + C = 0
            return [] if b == 0.0 else [-c / b]

        d = self.discriminant
        if d == 0.0:
            return [-b / (2.0 * a)]
        if d > 0.0:
            sq_d = math.sqrt(d)
            return [(-b + sq_d) / (2.0 * a), (-b - sq_d) / (2.0 * a)]
        return []

    def roots(self):
        '''
        Отсортированный список действительных корней уравнения.
        '''
        result = []
        for t in self._squares():
            result.extend(self._roots_from_square(t))
        return sorted(result)

    def print_solution(self):
        print('Уравнение:', self)
        if self.a != 0.0:
            print('Дискриминант D = {}'.format(self.discriminant))
        if self.is_identity:
            print('Корнем является любое действительное число')
            return
        roots = self.roots()
        if len(roots) == 0:
            print('Нет действительных корней')
        elif len(roots) == 1:
            print('Один корень: {}'.format(roots[0]))
        else:
            print('Корней: {} -> {}'.format(len(roots), ', '.join(str(r) for r in roots)))


def main():
    reader = CoefReader(sys.argv)
    equation = BiquadraticEquation(
        reader.read(1, 'Введите коэффициент А:'),
        reader.read(2, 'Введите коэффициент B:'),
        reader.read(3, 'Введите коэффициент C:'),
    )
    equation.print_solution()


if __name__ == "__main__":
    main()
