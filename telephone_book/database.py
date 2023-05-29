import view


def added(data):
    with open('db.txt', 'a') as file:
        file.write(data)
    print('Телефонная книга обнвлена')
    print('Выберите пункт меню')

def search(data_search):
    with open("db.txt", 'r') as file:
        data = file.readlines()
        x = False
        for i in data:
            if data_search in i:
                print(i)
                x == True
        if x == False:
                print('Таких данных нет в справочнике')

def sort_name():
    with open("db.txt", 'r') as file:
        data = file.readlines()
        data.sort()
        # print(data)
    with open("db.txt", 'w') as file:
        file.writelines(data)


def sort_date():
    with open("db.txt", 'r') as file:
        data = file.readlines()
        data.sort(key = lambda x: x[2])
        # print(data)
    with open("db.txt", 'w') as file:
        file.writelines(data)    

def print_name():
    with open("db.txt", 'r') as file:
        data = file.readlines()
        for i in data:
            print(i.split(';')[0])                

def read():
    with open("db.txt", 'r') as file:
        data = file.read()
        print(data)

def edit_data(str_edit):
    with open("db.txt", 'r') as file:
        data = file.readline()
    with open("db1.txt", 'w') as file1:
        for i in data:
            # print(i)
            if str_edit is None:
                file1.write(i)
                
                
            

