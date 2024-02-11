# Lesson 4
# Домашнее задание
# Работа с функциями и данными
#
# Цель:
# применить на практике пройденные на двух предыдущих семинарах темы
# использовать подходящие для решения задачи типы данных и применить нужные методы
# использовать операторы ветвления (if) и цикла (while, for)
# создать собственные функции


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
# my_first_func -> MyFirstFunc, AnotherFunction -> nother_function
def exercise_two() -> str:
    return ''


# Задание 3
# Написать функцию, которая принимает на вход квадратное уравнение (одной строкой) и возвращает его корни,
# либо сообщает, что их нет "x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7
def exercise_three():
    pass


# Задание 4
# Шифр Цезаря. Написать функцию, которая будет принимать два аргумента: слово (str) и ключ (int).
# Результат выполнения функции - шифрованое слово по методоту Шифр Цезаря. Написать вторую функцию,
# которая будет проводить обратный процесс (или написать одну, выполняющую оба действия)
# 'dog', 3 -> 'grj', 'python', 5 -> 'udymts'
def exercise_four():
    pass


if __name__ == '__main__':
    print(exercise_one())
print(exercise_two())
print(exercise_three())
print(exercise_four())
