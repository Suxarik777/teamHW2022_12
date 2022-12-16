from outputs import print_menu, menu_search, show_all, show_by_index, show_by_filter
from menu import change_menu_position
from edits import edit
from inputs import input_menu_item, input_row, input_index, input_string
from exports import export_file, export_csv, export_xml, export_html


menu_item = 0
array = [[]]
while menu_item != 7:
    print_menu()
    menu_item = input_menu_item()
    if menu_item == 1:
        input_row(array)
    elif menu_item == 2:
        ch_index = input_index(array)
        array = edit(ch_index, array)
    elif menu_item == 3:
        export_item = export_file()
        if export_item == 1:
            export_csv(array)
        if export_item == 2:
            export_xml(array)
        if export_item == 3:
            export_html(array)
    elif menu_item == 4:
        menu_search()
        search_item = input_menu_item()
        if search_item == 1:
            show_all(array)
        elif search_item == 2:
            show_item = input_menu_item()
            show_by_index(array, show_item)
        elif search_item == 3:
            search_item = input_string()
            show_by_filter(array, search_item)


#    menu_item_str = change_menu_position(menu_item)
