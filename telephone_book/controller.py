import view
import database


def main():
    while True:
        ask = view.user_input()
        if ask == 1:
            data = view.people()
            database.added(data)
        elif ask == 2:
            database.search(find)
        elif ask == 5:
            database.read()
        elif ask == 0:
            break
        # elif ask == 4:

        # elif ask == 5:
            # str = view.input_main()

main()
