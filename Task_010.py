# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите количество монеток: "))

count_tails = 0
count_emblem = 0
for i in range(n):
    var_side = input("Введите сторону: ")
    # var_side=int(input("Введите сторону: "))
    if var_side == "tails":
    # if var_side == 1:   
        count_tails += 1
    if var_side == "emblem":
    # if var_side == 0:
        count_emblem += 1        
if count_tails <= count_emblem:
    print(count_tails)
else:
    print(count_emblem)