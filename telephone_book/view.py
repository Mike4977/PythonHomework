def user_input():
    ask = int(input("Выбери ниже\n 1-ввод данных пользователя\n" 
                    "2-поиск по полю (телефон или имя)\n" 
                    "3-сортировка файла по имени и его перезапись\n" 
                    "4-сортировка файла по дате рождения и его перезапись\n" 
                    "5-вывод только имен\n 6-вывод всего файла txt \n 0-выход\n"))

    return ask

def people():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    date = input("Введите дату рождения: ")
    tel = input("Введите номер телефона: ")
    data = name + '; ' + surname + '; ' + date + '; ' + tel + '; ' +  '\n'
    print()
    return data


def search():
    str_find = input("Для поиска введите фамилию или номер телефона: ")
    return str_find

def edit_data():
    str_edit = input("Для изменения введите данные: ")
    return str_edit