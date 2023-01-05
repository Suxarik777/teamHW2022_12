from edits import delete_row, update_row, add_row


def menu(user, user_type, menu_item, users, notebook):
    if user_type == '1':
        admin(user, menu_item, users)
    elif user_type == '2':
        pupil(user, menu_item, notebook)
    elif user_type == '3':
        teacher(user, menu_item, notebook)


def admin(user, menu_item, users):
    if menu_item == 1:
        for item in users:
            if user != item[0]:
                print(item)
    elif menu_item == 2:
        for item in users:
            if user != item[0]:
                print(item)
        index = int(input('index to delete:'))
        delete_row(users, index)
    elif menu_item == 3:
        for item in users:
            if user != item[0]:
                print(item)
        index = int(input('index to update:'))
        update_row(users, index)
    elif menu_item == 4:
        add_row(users)
    return


def pupil(user, menu_item, notebook):
    if menu_item == 1:
        for item in notebook:
            if user == item[3]:
                print(item)
    return


def teacher(user, menu_item, notebook):
    if menu_item == 1:
        for item in notebook:
            if user != item[4]:
                print(item)
    elif menu_item == 3:
        for item in notebook:
            if user != item[4]:
                print(item)
        index = int(input('index to delete:'))
        delete_row(notebook, index)
    elif menu_item == 4:
        for item in notebook:
            if user != item[4]:
                print(item)
        index = int(input('index to update:'))
        update_row(notebook, index)
    elif menu_item == 5:
        add_row(notebook)
    return