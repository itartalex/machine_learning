# Lesson 4
# Домашнее задание
# Работа с функциями и данными
#
# Цель:
# применить на практике пройденные на двух предыдущих семинарах темы
# использовать подходящие для решения задачи типы данных и применить нужные методы
# использовать операторы ветвления (if) и цикла (while, for)
# создать собственные функции

import math


# Задание 1
# Описание/Пошаговая инструкция выполнения домашнего задания:
# Вводится целое число (любого размера). Написать функцию, которая разобьет это число на разряды символом "пробел",
# Функция возвращает тип данных str  1234567 -> 1 234 567, 267 -> 267, 34976 -> 34 976`
def exercise_one() -> str:
    num_str = str(input("Введите целое число: "))
    length_num_str = len(num_str)
    first_rank_num_str = ''.join(
        [num_str[:i] for i in range(0, length_num_str - 1, 1) if (length_num_str - i) % 3 == 0 and i <= 2])
    length_first_rank_num_str = len(first_rank_num_str)
    other_rank_num_str = ' '.join([num_str[i:i + 3] for i in range(length_first_rank_num_str, length_num_str - 1, 1) if
                                   (length_num_str - i) % 3 == 0])
    return first_rank_num_str + ' ' + other_rank_num_str


# Задание 2
# Написать функцию, которая заменяет принимает строку текста и изменяет снейк_кейс на КамелКейс и наоборот
# my_first_func -> MyFirstFunc, AnotherFunction -> another_function
def exercise_two() -> str:
    change_str = str(input("Введите текстовую строку: "))
    result_change_str = ''
    length_change_str = len(change_str)
    for i in range(0, length_change_str, 1):
        if change_str[i].isupper() and i == 0:
            result_change_str = result_change_str + change_str[i].lower()
        elif i == 0:
            result_change_str = result_change_str + change_str[i].upper()
        elif change_str[i] == "_":
            result_change_str = result_change_str + change_str[i + 1].upper()
        elif change_str[i].isupper():
            result_change_str = result_change_str + '_' + change_str[i].lower()
        else:
            result_change_str = result_change_str + change_str[i]

    return result_change_str


# Задание 3
# Написать функцию, которая принимает на вход квадратное уравнение (одной строкой) и возвращает его корни,
# либо сообщает, что их нет "x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7
def exercise_three():
    # x**2-11*x+28=0
    # a=1 b=-11 c=28
    # x_1=(-b-√dis)/2a  x_2=(-b+√dis)/2a   dis=b**2-4ac
    equation_str = str(input("Введите строку уравнения по шаблону x**2-11*x+28=0 :"))
    equation_str = equation_str.replace(' ', '')
    index_a = equation_str.find("x**2")
    index_b = equation_str.find('*x')
    index_c = equation_str.find('=0')
    a = 0
    b = 0
    c = 0
    if index_a == -1:
        pass
    elif index_a > 0:
        a = int(equation_str[:index_a])
    else:
        a = 1
    if index_b == -1:
        pass
    elif index_b - (index_a + 4) > 1:
        b = int(equation_str[index_a + 4:index_b])
    else:
        b = int(equation_str[index_a + 4:index_b] + 1)
    if index_c == -1:
        pass
    elif index_c - (index_b + 2) > 1:
        c = int(equation_str[index_b + 2:index_c])
    dis = b ** 2 - 4 * a * c
    if dis > 0:
        x_1 = (-b - math.sqrt(dis)) / (2 * a)
        x_2 = (-b + math.sqrt(dis)) / (2 * a)
        print(f"x_1 = {x_1} x_2 = {x_2}")
    elif dis == 0:
        x = -b / (2 * a)
        print(f"x_1 = x_2 = {x}")
    else:
        print("Корней нет")


# Задание 4
# Шифр Цезаря. Написать функцию, которая будет принимать два аргумента: слово (str) и ключ (int).
# Результат выполнения функции - шифрованое слово по методоту Шифр Цезаря. Написать вторую функцию,
# которая будет проводить обратный процесс (или написать одну, выполняющую оба действия)
# 'dog', 3 -> 'grj', 'python', 5 -> 'udymts'
# шифрование
def exercise_four_encryption():
    cipher_word = str(input("Введите слово для шифрования:"))
    cipher_key = int(input("Введите ключ:"))
    result = []
    dict_lang = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(cipher_word)):
        for j in range(len(dict_lang)):
            if 0 <= j + cipher_key < len(dict_lang) and cipher_word[i] == dict_lang[j]:
                result.append(dict_lang[j + cipher_key])
            elif j + cipher_key >= len(dict_lang) and cipher_word[i] == dict_lang[j]:
                result.append(dict_lang[(1 - j - cipher_key) % (len(dict_lang) - 1)])
            elif j + cipher_key < 0 and cipher_word[i] == dict_lang[j]:
                result.append(dict_lang[(j + cipher_key) % len(dict_lang)])
    print(''.join(result))


# дешифрование
def exercise_four_decryption():
    cipher_word = str(input("Введите слово для дешифрования:"))
    cipher_key = -int(input("Введите ключ:"))
    result = []
    dict_lang = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(cipher_word)):
        for j in range(len(dict_lang)):
            if 0 <= j + cipher_key < len(dict_lang) and cipher_word[i] == dict_lang[j]:
                result.append(dict_lang[j + cipher_key])
            elif j + cipher_key >= len(dict_lang) and cipher_word[i] == dict_lang[j]:
                result.append(dict_lang[(1 - j - cipher_key) % (len(dict_lang) - 1)])
            elif j + cipher_key < 0 and cipher_word[i] == dict_lang[j]:
                result.append(dict_lang[(j + cipher_key) % len(dict_lang)])
    print(''.join(result))


if __name__ == '__main__':
    print(exercise_one())
    print(exercise_two())
    exercise_three()
    exercise_four_encryption()
    exercise_four_decryption()
