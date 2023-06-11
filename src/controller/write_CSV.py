def add_note(list=[]):
    with open("data/notes.CSV", "a", encoding="UTF-8") as data_file:
        data_file.write(";".join(list))
        data_file.write("\n")
