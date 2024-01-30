"""
Урок 3, задача 2.
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
"""

import re
from collections import Counter

import sys
import traceback
import logging
from sys import stdout

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler("tmp.log", mode="a"),
        logging.StreamHandler(stdout)
    ],
    format="[%(asctime)s] [%(levelname)s] [%(func_name)s] [%(message)s]"
)


def logger(message='function', skip=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            extra = {'func_name': func.__name__}
            try:
                result = func(*args, **kwargs)
                logging.info(message, extra=extra)
                return result
            except Exception as ex:
                logging.error(message, extra=extra)
                logging.error(ex, extra=extra)
                logging.error(f"{args} || {kwargs}", extra=extra)
                description = traceback.format_exception(*sys.exc_info())
                logging.error(f"\n {''.join(description)}", extra=extra)
                if not skip:
                    raise
        return wrapper
    return decorator


@logger(skip=False)
def word_counter(text):
    return sorted(list(Counter([i.lower() for i in re.findall('[a-zA-Zа-яА-ЯёЁ]+', text)]).items()),
                  key=lambda x: x[1],
                  reverse=True)[:10]


def main():
    text = 'Hello world. Hello Python. Hello again.'
    print(word_counter(text))


if __name__ == '__main__':
    main()
