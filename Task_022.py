# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений 
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь 
# вводит сами элементы множеств.

n = int(input("длина первого списка:  "))
lst1 = []
n1 = []
for i in range(n):
    lst1.append(int(input()))
n1 = set(lst1)
    
m = int(input("длина второго списка:  "))
lst2 = []
m1 = []
for j in range(m):
    lst2.append(int(input()))
m1 = set(lst2)
print(n1)
print(m1)
list = []
for i in n1:
    for j in m1:
        if j == i:
            list.append(j)
print(list)
# lst11 = set(lst1)
# lst21 = set(lst2)
# print(*lst11)
# print(*lst21)


# c = []
# for i in range(len(lst11)):
#     for j in range(len(lst21)):
#         if lst1[i] == lst2[j]:
#            c[i] = (lst1[i])
# print(c)

