def print_menu(user):
    return

import csv
from menu import admin, pupil, teacher


def print_array(array):
    return


def print_menu(user_type):
    if user_type == '1':
        print(F' Show 1 \n Delete 2 \n Update 3 \n Add 4 \n Exit 8')
    elif user_type == '2':
        print(F' Show all 1 \n Show by date 2 \n Exit 8')
    elif user_type == '3':
        print(F' Show all 1 \n Show by date 2 \n Delete 3 \n Update 4 \n Add 5 \n Exit 8')

'''
def print_array(array, user, user_type):
    with open(source_path, 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
        info = []
        for row in file_reader:
            if user in row:
                info.append(row)
    return info
'''


def print_aray_search(array, search_string):
    return
    with open(source_path, 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
        info = []
        for row in file_reader:
            if search_string in row:
                info.append(row)
    return infourn