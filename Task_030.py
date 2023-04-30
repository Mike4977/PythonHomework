# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def progression(a, d, n):
    arr = [a]
    for i in range(2, n + 1):
        a1 = a + d * (i - 1)
        arr.append(a1)
    return arr


def progression(a, d, n):
    arr = []
    for i in range(n):
        arr.append(a + d * (i - 1))
    return arr

a = int(input("Введите первый элемент прогрессии a = "))
d = int (input("Введите разность элементов d = "))
n = int(input("Введите количество элементов n = "))

print(progression(a, d, n))
