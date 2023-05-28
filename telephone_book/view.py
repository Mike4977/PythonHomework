def user_input():
    ask = int(input("Выбери ниже\n 1-ввод данных пользователя\n 2-поиск по имени\n 3-поиск по полю (телефон или имя)\n 4-сортировка файла по имени или по дате рождения и его перезапись\n 5-вывод только имен\n 6-вывод всего файла txt \n 0-выход\n"))

    return ask

def people():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    date = input("Введите дату рождения: ")
    tel = input("Введите номер телефона: ")
    data = name + '; ' + surname + '; ' + date + '; ' + tel + '; ' +  '\n'
    # lst_data = [data]
    print()
    return data
# print(people())

# def search_name():
#     str_find = input("Введите фамилию для поиска:  " )
#     return str_find

def search():
    str_find = input("Для поиска введите фамилию или номер телефона: ")
    return str_find