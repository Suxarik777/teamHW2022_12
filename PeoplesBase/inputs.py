from PhoneBook.inputs import input_string as str_input

#
# def menu_input(user_type):
#     return menu_item

import csv
import os
from pathlib import Path

from outputs import print_menu


def menu_input():
    menu_item = int(input('Input menu Item\n'))
    return menu_item


def str_input():
    return input('Input search string')


def input_file(source_path):
    with open(source_path, 'r', encoding='utf-8') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', skipinitialspace=False)
        data_list_file = list(file_reader)
    return data_list_file
