import time
from contextlib import contextmanager


class cm_timer_1:
    """
    Контекстный менеджер на основе класса.
    """

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('time: {:.3f}'.format(time.perf_counter() - self.start))
        # Исключения из блока не подавляются
        return False


@contextmanager
def cm_timer_2():
    """
    Контекстный менеджер с использованием библиотеки contextlib.
    """
    start = time.perf_counter()
    try:
        yield
    finally:
        print('time: {:.3f}'.format(time.perf_counter() - start))


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(1.5)

    with cm_timer_2():
        time.sleep(1.5)
