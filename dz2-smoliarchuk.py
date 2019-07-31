# Пользователь вводит свое имя и возраст вывести строку в формате - “Hello {username} your age is {age}”, заменить текст в фигурных скобках на значения введенные пользователем.

username = input("Enter your name: ")
age = input("Enter your age: ")

if __name__ == "__main__":
    print(f"Hello {username}, your age is {age}.")

# Пользователь вводит число, вывести его в 132 степени и Показать его остаток от деления на 3. Вывод должен быть в одну строку с пояснениями.

user_input = input("Enter a number: ")
exp = int(user_input) ** 132
mod = exp % 3

if __name__ == "__main__":
    print(f"Your number in 132 degrees is {exp}. The remainder of dividing by 3 is {mod}.")

# Пользователь вводит 2 числа вывести каждую математическую операцию для этих чисел. Каждая новая операция должна быть выведена с новой строки с  пояснением.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if __name__ == "__main__":
    print(f"{num1 + num2} # Addition of numbers")
    print(f"{num1 - num2} # Subtraction of numbers")
    print(f"{num1 * num2} # Multiplication of number")
    print(f"{num1 / num2} # Division(float) of number")
    print(f"{num1 // num2} # Division(floor) of number")
    print(f"{num1 ** num2} # Exponentiation of number")
    print(f"{num1 % num2} # Modulo of both number")

# Пользователь вводит 3 числа, подставить и посчитать формулу: 2a - 8b / (a-b+c). Вывести результат.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

if __name__ == "__main__":
    print(2 * num1 - 8 * num2 / (num1 - num2 + num3))

# Пользователь вводит строку и число, вывести повторение строки равное введенному числу. Вывод должен быть в одну строку.

str1 = input("Enter a stroke: ")
num1 = int(input("Enter a number: "))

if __name__ == "__main__":
    print(str1 * num1)

# Даны числа 125 и 437 вывести их остатки от деления на 2, 3, 10, 22 с пояснениями.

FIRST = 125
SECOND = 437

if __name__ == "__main__":
    print(f"Остаток от деления {FIRST} на 2 = {FIRST % 2}\n"
          f"Остаток от деления {FIRST} на 3 = {FIRST % 3}\n"
          f"Остаток от деления {FIRST} на 10 = {FIRST % 10}\n"
          f"Остаток от деления {FIRST} на 22 = {FIRST % 22}")
    print(f"Остаток от деления {SECOND} на 2 = {SECOND % 2}\n"
          f"Остаток от деления {SECOND} на 3 = {SECOND % 3}\n"
          f"Остаток от деления {SECOND} на 10 = {SECOND % 10}\n"
          f"Остаток от деления {SECOND} на 22 = {SECOND % 22}")

# Пользователь вводит 2 числа, вывести целую часть от деления одного на другое.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if __name__ == "__main__":
    print(num1 // num2)

# Пользователь  вводит 3 строки. Вывести их в одну строку разделенные пробелом. В этой задаче метод print может принимать только один параметр.

str1 = input("Enter a first stroke: ")
str2 = input("Enter a second stroke: ")
str3 = input("Enter a third stroke: ")

list = [str1, str2, str3]

if __name__ == "__main__":
    print(''.join(list))

# Даны два числа first = 15 second = 43, записать first в second, a second в first. Вывести

FIRST = 15
SECOND = 43

FIRST, SECOND = SECOND, FIRST

if __name__ == "__main__":
    print(FIRST, SECOND)
