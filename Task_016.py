# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


n = int(input("Введите количество элементов в массиве: "))
x = int(input("Введите число X: "))
# numb = [0] * n  # вариант 1
numb = [] # вариант 2
count = 0
for i in range(n):
    # numb[i] = int(input("Введите элементы массива: ")) # вариант 1
    numb.append(i) # вариант 2
    # print(numb)
    if numb[i] == x:
        count += 1
print(*numb)
print("->", count)

