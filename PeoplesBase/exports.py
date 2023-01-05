def export_csv(arr, name_file):
    with open(f'{name_file}.csv', 'w', encoding='utf-8') as file:
        for line in arr:
            res_text = ''
            for item in line:
                res_text += str(item) + ';'
            file.writelines(f'{res_text}; \n')


def export_files(users, notebook):
    export_csv(users, 'user')
#    export_csv(user_types, 'user_types')
#    export_csv(subjects, 'subjects')
    export_csv(notebook, 'notebook')