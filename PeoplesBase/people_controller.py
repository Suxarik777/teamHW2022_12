from login import login
from init import import_files
from exports import export_files
from checks import check_user
from outputs import  print_menu
from inputs import menu_input
from menu import admin, pupil, teacher

users, user_types, subjects, notebook = import_files()
user = login()
user_type = check_user(user, users)
menu_item = 0
while menu_item != 8:
	print_menu(user_type)
	menu_item = menu_input(user)
	if menu_item == 1:
		admin(users, user_types, user)
	elif menu_item == 2:
		pupil(users, user, notebook)
	elif menu_item == 3:
		teacher(users, user, notebook)
export_files(users, user_types, subjects, notebook)
