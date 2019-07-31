# Написать декоратор который будет выводить на экран время выполнения функции.

# import time
#
#
# def time_of_function(func):
#     def wrapper(*args):
#         start_time = time.clock()
#         res = func(*args)
#         print(f'[*] Время выполнения: {time.clock() - start_time} секунд.')
#         return res
#     return wrapper
#
#
# @time_of_function
# def some_method(a, b):  # пример взял из листинга занятия
#     time.sleep(2)
#     return a + b
#
#
# print(some_method(31, 76))


# Сформировать убывающий массив из чисел, которые делятся на 3. Длину вводит пользователь

# len_of_array = input("Len of array: ")
#
# if len_of_array.isdigit():
#     for i in reversed(range(3, int(len_of_array), 3)):
#         quotient = i / 3
#         print(int(i), end=' ')
# else:
#     print("Len type is not a digit!")

# Написать декоратор skip который не выполняет функцию.
# Декоратор может принимать параметр который выдаст функция вместо реального результата

# import time
#
#
# def skip(result=None):
#     def wrapped_wrapper(func):
#         def wrapper(*args, **kwargs):
#             if result:
#                 return result
#             else:
#                 print("Function has been skipped")
#         return wrapper
#     return wrapped_wrapper
#
#
# @skip(result=55)
# def some_method(a, b):  # пример взял из листинга занятия
#     time.sleep(2)
#     return a + b


# print(some_method(31, 76))


# Напишите генератор генерирующий последовательность треугольных чисел.

# def triangle(n):
#     for i in range(1, n):
#         trg1 = i * (i + 1) / 2
#         yield trg1
#
#
# for trg in triangle(20):
#     print(int(trg), end=' ')
