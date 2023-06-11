import src.controller.notes_collection as notes_collection


def act(list_input=[], notes=notes_collection.Notes_collection()):
    if list_input[0] == "1":
        notes.create_new_note(list_input[1][0], list_input[1][1])
    if list_input[0] == "2":
        print(notes)
    if list_input[0] == "3":
        if notes.edit_note(list_input[1], list_input[2][0], list_input[2][1]) != True:
            print("There is no such index")
    if list_input[0] == "4":
        print(notes.show_by_date(list_input[1]))
    if list_input[0] == "5":
        if notes.delete_by_index(list_input[1]) != True:
            print("There is no such index")
