import src.menu.menu_controller as menu
import src.controller.notes_collection as notes

notes_lst = notes.Notes_collection()
notes_lst.create_new_note("h1", "v1")
notes_lst.create_new_note("h2", "v2")
notes_lst.create_new_note("h3", "v3")
notes_lst.create_new_note("h4", "v4")
print(notes_lst)
print(f"del {notes_lst.delete_by_index(2)}")
print(f'edit {notes_lst.edit_note("h5", "v6", 3)}')
notes_lst.create_new_note("v7", "v7")
notes_lst.create_new_note("v8", "v8")

print(notes_lst.show_by_date("11.6.2023"))

"""print(menu.start())"""
