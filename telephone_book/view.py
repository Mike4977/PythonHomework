def user_input():
    ask = int(input("Выбери ниже\n 1-ввод данных пользователя\n "
                    "2-поиск по полю (телефон или имя)\n "
                    "3-сортировка файла по имени и его перезапись\n "
                    "4-сортировка файла по дате рождения и его перезапись\n "
                    "5-вывод только имен\n 6-вывод всего файла txt \n "
                    "7-удаление данных\n 8-изменение данных\n 0-выход\n"))

    return ask

def people():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    date = input("Введите год рождения: ")
    tel = input("Введите номер телефона: ")
    data = name + '; ' + surname + '; ' + date + '; ' + tel + '; ' +  '\n'
    print()
    return data.lower()


def search():
    str_find = input("Введите данные для поиска: ").lower()
    return str_find

def delete_data():
    str_data = input("Введите данные для удаления : ").lower()
    return str_data

def select_num():
    number = int(input("Введите номер  строки: "))
    return number

def edit_data():
    str_data = input("Введите данные для редактирования: ").lower()
    return str_data

