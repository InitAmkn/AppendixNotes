import src.controller.notes_collection as notes_collection


def refresh(notes=notes_collection.Notes_collection().all_notes):
    with open("data/notes.CSV", "w", encoding="UTF-8") as data_file:
        for i in notes:
            data_file.write(
                f"{i};{notes[i].heading};{notes[i].body};{notes[i].date_of_creation}")
            data_file.write("\n")
