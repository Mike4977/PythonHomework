# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке


# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def poem_rhythm(str):
    str = str.split()
    list = []
    for phrase in str:
        count = 0
        for i in phrase:
            if i in 'аеёиоуыэюя':
                count += 1
        list.append(count)
        print(list)
    print(list.count(list[1]))
    return len(list) == list.count(list[1]) # list.count(list[1]) - считает одинаковые элементы списка
    
string = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if poem_rhythm(string):
    print('Парам пам-пам')
else:
    print('Пам парам')



# # vowels list
# vowels = ['a', 'e', 'i', 'o', 'i', 'u'] 
# # count element 'i' 
# count = vowels.count('i') 
# # print count 
# print('The count of i is:', count) 
# # count element 'p' 
# count = vowels.count('p') 
# # print count 
# print('The count of p is:', count)