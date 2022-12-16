from outputs import print_menu, menu_search
from menu import change_menu_position
from edits import edit
from inputs import input_menu_item, input_row, input_index, input_string, input_file
from exports import export_file, export_csv, export_xml, export_html


menu_item = 0
array = [[]]
while menu_item != 7:
    #print_menu()
    menu_item = input_menu_item()
    if menu_item == 1:
        array = input_row()
    elif menu_item == 2:
        ch_index = input_index()
        array = edit(ch_index, array)
    elif menu_item == 3:
        #export_file()
        export_item = export_file()
        data_list_file = input_file('Spraw2.csv')
        if export_item == 1:
            export_csv(data_list_file)
        if export_item == 2:
            export_xml(data_list_file)
        if export_item == 3:
            export_html(data_list_file)
    elif menu_item == 4:
        menu_search()
        search_item = input_menu_item()



#    menu_item_str = change_menu_position(menu_item)
