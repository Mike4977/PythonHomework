import view


def added(data):
    with open('db.txt', 'a', encoding="UTF-8") as file:
        file.write(data)
    print('Телефонная книга обнвлена')
    print('Выберите пункт меню')

def search(data_search):
    with open("db.txt", 'r', encoding="UTF-8") as file:
        data = file.readlines()
        x = False
        for i in data:
            if data_search in i:
                print(i)
                x == True
        if x == False:
                print('Таких данных нет в справочнике')

def sort_name():
    with open("db.txt", 'r', encoding="UTF-8") as file:
        data = file.readlines()
        data.sort()
        # print(data)
    with open("db.txt", 'w', encoding="UTF-8") as file:
        file.writelines(data)


def sort_date():
    with open("db.txt", 'r', encoding="UTF-8") as file:
        data = file.readlines()
        data.sort(key = lambda x: x[2])
        # print(data)
    with open("db.txt", 'w', encoding="UTF-8") as file:
        file.writelines(data)    

def print_name():
    with open("db.txt", 'r', encoding="UTF-8") as file:
        data = file.readlines()
        for i in data:
            print(i.split(';')[0])                

def read():
    with open("db.txt", 'r', encoding="UTF-8") as file:
        data = file.read()
        print(data)

def select_people(data):
    lst = []
    count = 1
    with open("db.txt", 'r', encoding="UTF-8") as file:
        lst_str = file.readlines()
        for people in lst_str:
                if data in people:
                    print(f"{count}) {people.strip()}")
                    count+=1
                    lst.append(people)
    return lst
                
def delete_str(data):
    with open("db.txt", 'r', encoding="UTF-8") as file:
        old_lst = file.readlines()
    with open("db.txt", 'w', encoding="UTF-8") as file:
        for people in old_lst:
            if data == people:
                continue
            file.write(people)
    print("Данные удалены")

def edit_str(data):
    with open("db.txt", 'r', encoding="UTF-8") as file:
        old_lst = file.readlines()
    with open("db.txt", 'w', encoding="UTF-8") as file:
        for people in old_lst:
            if data == people:
                new_data = view.people()
                file.write(new_data)
                continue
            file.write(people)
    print("Данные изменены")
        
