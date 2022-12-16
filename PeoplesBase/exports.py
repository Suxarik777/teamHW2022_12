from PhoneBook.exports import export_csv

def export_files(users, user_types, subjects, notebook):
    export_csv(users, 'users')
    export_csv(user_types, 'user_types')
    export_csv(subjects, 'subjects')
    export_csv(notebook, 'notebook')