# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

s=int(input("Сколько сделали журавликов  "))
if s%6!=0:
    print("На производстве что-то пошло не так")
else:
    print("Петя сделал", s//6, "журавликов")
    print("Сережа сделал", s//6, "журавликов")
    print("Катя сделала", s//6*4, "журавликов")
    
    