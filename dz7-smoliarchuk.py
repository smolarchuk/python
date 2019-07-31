# Дан файл с текстом, создать список из дат в тексте - даты в формате DD-MM-YYYY (02-03-1999)

# import re

# ! через ваши подсказки так и не заработало:
# with open("text_file.txt", 'r') as text:
#     dates = []
#     a = re.findall(r'3[01]|[12][0-9]|0[1-9]-1[012]|0[1-9]-\d{4}', str(text.readlines()))
#     for date in a:
#         dates.append('-'.join([x for x in date]))
#     print(dates)

# ! заработало как надо только если не проверять дату на количество дней и месяцев:
# with open("text_file.txt", 'r') as text:
#     print(re.findall(r'([0-9]{2}-[0-9]{2}-\d{4})\b', str(text.readlines())))


# Пользователь вводит год в формате - YYYY (1999) Определить, является ли год високосным

# import calendar
# import re
#
# year = input("Year (YYYY): ")
# if re.findall(r'\d{4}', year):
#     print(calendar.isleap(int(year)))
# else:
#     print("Year has incorrect format.")


# Дан файл вывести сумму всех чисел в файле. Цифры могут быть не целыми и отрицательными

# import re
#
# with open("text_file.txt", 'r') as text:
#     print(sum(map(float, re.findall(r'-?\d+\.?\d+\b', str(text.readlines())))))


# Написать генератор геометрической прогрессии

# def geometric_progression(start=1, n=10, q=3):
#     value = start
#
#     for i in range(n):
#         yield value
#
#         value *= q
#
#
# for x in geometric_progression():
#     print(x)


# Дан файл с текстом, удалить из файла все отрицательные числа, числа могут быть не целыми

# import re
#
# with open("text_file.txt", 'r') as text, open("output_file.txt", 'w') as file:
#     file.write(re.sub(r'[^\w](-\d+\.?\d+)\b', "", str(text.readlines())))


# Дан файл с текстом, вывесли список который содержит все имена, все фамилии и все географические названия.

# import re

# with open("text_file.txt", 'r') as text:
#     print(re.findall(r'[^\.] ([A-Z][a-z]+)', str(text.readlines())))
