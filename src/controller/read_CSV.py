import src.controller.notes_collection as notes_collection
import src.controller.note as note


def file_notes():
    with open("data/notes.CSV", "r", encoding="UTF-8") as data_file:
        notes = list(data_file.readlines())
        notes = [notes[i].replace("\n", "").split(";")
                 for i in range(len(notes))]
        notes_dictionary = {}
        for i in notes:
            if i[0].isdigit:
                notes_dictionary[int(i[0])] = note.Note(
                    i[1], i[2], i[3])
        return notes_dictionary
