from colorama import init
from colorama import Fore, Back, Style
init()

#This is comment

print(Back.WHITE)
print(Fore.BLACK)
what = input("Что делаем (+, -): ")

a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

print(Back.GREEN)
if what == "+":
	c = a + b

	print("Результат : " + str(c))

elif what == "-":
    c = a - b
    print("Результат : " + str(c))

else:
    print("Выбрана неверная операция!")
