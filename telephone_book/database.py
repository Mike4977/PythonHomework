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

def read():
    with open("db.txt", 'r') as file:
        data = file.read()
        print(data)

