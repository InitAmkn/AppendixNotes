import src.terminal.request as request
import src.terminal.menu_data as menu
import src.terminal.comand_controller as comand
import src.controller.notes_collection as notes_collection
import src.controller.write_CSV as write_CSV
import src.controller.read_CSV as read_CSV


def terminal():
    notes = notes_collection.Notes_collection()
    notes.all_notes = read_CSV.file_notes()
    while (True):
        list_input = []
        list_input.append(request.choice(menu.action))
        if list_input[len(list_input)-1] == "1":
            list_input.append(request.input_note(menu.add_note))
        if list_input[len(list_input)-1] == "3":
            list_input.append(request.input_index(menu.enter_index))
            list_input.append(request.input_note(menu.add_note))
        if list_input[len(list_input)-1] == "4":
            list_input.append(request.input_date(menu.enter_date))
        if list_input[len(list_input)-1] == "5":
            list_input.append(request.input_index(menu.enter_index))
        comand.act(list_input, notes)
        write_CSV.refresh(notes.all_notes)
