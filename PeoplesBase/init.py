from PhoneBook.inputs import input_file


def import_files():
    users = input_file('users.csv')
    users_type = input_file('user_type.csv')
    subjects = input_file('subject.csv')
    notebook = input_file('notebook.csv')
    return users, users_type, subjects, notebook