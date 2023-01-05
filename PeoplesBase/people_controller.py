from login import login
from init import import_files
from exports import export_files
from outputs import print_menu
from inputs import menu_input
from menu import menu

users, notebook = import_files()
user, user_type = login()
menu_item = 0
while menu_item != 8:
	print_menu(user_type)
	menu_item = menu_input()
	menu(user, user_type, menu_item, users, notebook)
export_files(users, notebook)
