import view
import database


def main():
    while True:
        ask = view.user_input()
        if ask == 1:
            data = view.people()
            database.added(data)
        elif ask == 2:
            find = view.search()
            database.search(find)
        elif ask == 3:
            database.sort_name()
        elif ask == 4:
            database.sort_date()    
        elif ask == 5:
            database.print_name()
        elif ask == 6:
            database.read()
        elif ask == 7:
            _edit = view.edit_data()
            database.edit_data(_edit)
        elif ask == 0:
            break
        
main()


