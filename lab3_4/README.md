# Лабораторная работа №3-4. Функциональные возможности языка Python

**Цель:** изучение возможностей функционального программирования в языке Python.

Решения находятся в пакете `lab_python_fp`, по одному файлу на задачу. При запуске каждый файл печатает результаты своих тестов.

| Задача | Файл | Содержание |
|---|---|---|
| 1 | `field.py` | генератор `field(items, *args)` — значения полей из списка словарей |
| 2 | `gen_random.py` | генератор `gen_random(num_count, begin, end)` — случайные числа |
| 3 | `unique.py` | итератор `Unique(items, **kwargs)` — пропуск дубликатов, `ignore_case` |
| 4 | `sort.py` | сортировка по модулю через `sorted`, с `lambda` и без неё |
| 5 | `print_result.py` | декоратор `print_result` |
| 6 | `cm_timer.py` | контекстные менеджеры `cm_timer_1` (класс) и `cm_timer_2` (`contextlib`) |
| 7 | `process_data.py` | обработка списка вакансий цепочкой `f1 → f2 → f3 → f4` |

## Запуск

```bash
cd lab_python_fp
python3 field.py
python3 gen_random.py
python3 unique.py
python3 sort.py
python3 print_result.py
python3 cm_timer.py
python3 process_data.py ../data_light.json
```

Файл с данными (14 МБ) не хранится в репозитории. Скачать его:

```bash
curl -L -o data_light.json https://raw.githubusercontent.com/ugapanyuk/BKIT_2021/main/notebooks/fp/files/data_light.json
```

Если путь к файлу не передан, `process_data.py` ищет `data_light.json` в папке `lab3_4`.

## Примеры выполнения

```
$ python3 field.py
field(goods, 'title'):
['Ковер', 'Диван для отдыха', 'Стелаж']
field(goods, 'title', 'price'):
[{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха'}, {'title': 'Стелаж', 'price': 7000}]
field(goods, 'title', 'price', 'color'):
[{'title': 'Ковер', 'price': 2000, 'color': 'green'}, {'title': 'Диван для отдыха', 'color': 'black'}, {'color': 'white'}, {'title': 'Стелаж', 'price': 7000}]

$ python3 gen_random.py
gen_random(5, 1, 3): [1, 3, 1, 3, 1]
gen_random(10, -5, 5): [-1, -1, 2, 4, 2, 2, 3, -3, -5, 4]

$ python3 unique.py
Unique([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]): [1, 2]
Unique(gen_random(10, 1, 3)): [3, 2, 1]
Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']): ['a', 'A', 'b', 'B']
Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'], ignore_case=True): ['a', 'b']

$ python3 sort.py
[123, 100, -100, -30, 30, 4, -4, 1, -1, 0]
[123, 100, -100, -30, 30, 4, -4, 1, -1, 0]

$ python3 print_result.py
!!!!!!!!
test_1
1
test_2
iu5
test_3
a = 1
b = 2
test_4
1
2

$ python3 cm_timer.py
time: 1.505
time: 1.505

$ python3 process_data.py ../data_light.json
f1
1С программист
2-ой механик
...
f4
Программист с опытом Python, зарплата 169247 руб.
Программист / Senior Developer с опытом Python, зарплата 109006 руб.
Программист 1С с опытом Python, зарплата 132618 руб.
...
time: 0.003
```
