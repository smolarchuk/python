# Дан текст (любой, можете использовать - lorem ipsum) посчитать количество слов и предложений в тексте.

TEXT1 = """
What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

clean_text = TEXT1.rstrip().lstrip()
while "  " in TEXT1:
    clean_text = TEXT1.replace("  ", " ")
if __name__ == "__main__":
    print(f"Words count: {clean_text.count(' ')+1}. "
          f"Sentences count: {clean_text.count('.') + clean_text.count('!') + clean_text.count('?')}")

# Пользователь вводит число, если оно четное вывесть - “Even” если нет - “Odd”

number = input('Enter a number: ')

if number.isdigit():
    if int(number) % 2 == 0:
        print("It's even")
    else:
        print("Its odd")
else:
    print('Seams like a float or string')

# Пользователь вводит значения через запятую, если количество значений меньше 10, отсортировать их от большего к меньшему, если больше то от меньшего к большему.

list1 = input("Enter numbers separated by commas: ").split(',')

if len(list1) < 10:
    print(sorted(list1, reverse=True))
else:
    print(sorted(list1))

# Пользователь вводит 2 числа, если первое больше второго, вывести их разность, если второе больше первого вывести их сумму, если числа равны, возвести первое в степень второго.

num1 = input("Enter a first number: ")
num2 = input("Enter a second number: ")

if num1.isdigit() and num2.isdigit():
    if num1 > num2:
        print(f"Sub of this numbers is {num1 - num2}")
    elif num1 < num2:
        print(f"Add of this numbers is {num1 + num2}")
    else:
        print(f"Exp of this numbers is {num1 ** num2}")
else:
    print("Your numbers is incorrect!")

# Пользователь вводит 3 числа, подставить и посчитать формулу: 2a - 8b / (a-b+c). Вывести результат.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(f"2 * {a} - 8 * {b} / ({a} - {b} + {c}) = {2 * a - 8 * b / (a - b + c)}")

# Дан список из целых чисел длиной N подсчитать количество четных чисел в списке

LIST1 = [1, 2, 3, 4, 5, 6]

even = 0

for x in LIST1:
    if x % 2 == 0:
        even += 1

print("Even: ", even)

# Дан список целых чисел длиной N отсортировать список, не используя метода sort или sorted. (Пожалуйста не гуглите решение, постарайтесь сделать сами)

LIST1 = [1, 5, 3, 6, 2, 4]

print(list(set(LIST1)))

# Рассчитать последовательность фибоначчи, длину ряда задает пользователь

n = int(input("Введите длину ряда: "))
fib = [0, 1]
while len(fib) < n:
    fib.append(fib[-2] + fib[-1])

print(fib)

# Пользователь вводит целое число, определить простое ли оно.

num1 = int(input("Enter a number: "))
if num1 > 1:
    for x in range(2, num1):
        if (num1 % x) == 0:
            print(num1, "is not a prime number")
            print(x, "times", num1 // x, "is", num1)
            break
    else:
        print(num1, "is a prime number")

else:
    print(num1, "is not a prime number")
