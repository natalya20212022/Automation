import math


def square(a):
    a = math.ceil(a)
    s = a * a
    return s


a = input("Сторона квадрата: ")
side = float(a)
result = square(side)
print(f"Площадь квадрата: {result}")
