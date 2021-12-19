#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Объявите функцию, которая принимает строку на кириллице
и преобразовывает ее в латиницу, используя следующий словарь
для замены русских букв на соответствующее латинское написание:
"""


def decorator(func):
    start = " !?:;,."

    def wrapper(s):
        temp = func(s)
        temp = temp.replace('?', '-')
        temp = temp.replace('!', '-')

        # Проходит по списку
        for i, item in enumerate(temp):
            # Если встречается первый -
            if item == '-':
                # Проходит дальше и удаляет следующие -
                for value in temp[i+1:]:
                    if value == '-':
                        temp = temp.replace(value, '', 1)
                    else:
                        break

        return temp

    return wrapper


@decorator
def transliteration(s):
    s = s.lower()
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
         'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
         'н': 'n',  'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
         'ф': 'f',  'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
         'ъ': '',   'ы': 'y', 'ь': '',  'э': 'e',  'ю': 'yu', 'я': 'ya'}

    temp = ""

    for i in s:

        for v in t:
            if i == v:
                temp += t[v]
                break
        else:
            temp += i

    return temp


if __name__ == '__main__':
    st = str(input("Введите строку русскими буквами: "))
    print("Транслитерация строки: ", transliteration(st))
