# Дан список с произвольнвми элементами. Проверить все ли элементы списка не уникальны

# LIST = [1, 1, 2, 2, 3, 3, 4, 4]
#
#
# def no_unique(list1):
#     print(all([(list1.count(i) > 1) for i in set(list1)]))
#
#
# no_unique(LIST)


# Написать функцию которая принимает номер тролейбусного билета и определяет счастливый
# (сумма первых трех цифр == сумма последних трех цифр) или нет, а так же предидущий и следующий счастливые билеты.
# Функция должна валидировать то что номер 6ти значный и если нет кидать исключение - NotValidTicketNumber


# def ticket(number):
#     try:
#         if str(number).isdigit and len(str(number)) == 6 and 0 < int(number) < 1000000:
#             check = [int(i) for i in str(number)]
#             if sum(check[:3]) == sum(check[-3:]):
#                 return True
#             else:
#                 return False
#         else:
#             raise Exception("NotValidTicketNumber")
#     except ValueError:
#         raise Exception("NotValidTicketNumber")
#
#
# in_number = input("Enter a number of ticket: ")
#
# if ticket(in_number):
#     print("Your ticket is Luck")
# else:
#     print("Your ticket is not Luck")
#
# for x in range(int(in_number) + 1, 1000000):
#     if ticket(str(x).zfill(6)):
#         print(f"Next Lucky ticket is {str(x).zfill(6)}")
#         break
# else:
#     print("No next Lucky tickets found")
#
# for x in reversed(range(1, int(in_number))):
#     if ticket(str(x).zfill(6)):
#         print(f"Previous Lucky ticket is {str(x).zfill(6)}")
#         break
# else:
#     print("No previous Lucky tickets found")

