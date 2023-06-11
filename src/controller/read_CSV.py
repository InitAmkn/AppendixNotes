def file_notes():
    with open("data/notes.CSV", "r", encoding="UTF-8") as data_file:
        persons = list(data_file.readlines())
        persons = [persons[i].replace("\n", "").split(";")
                   for i in range(len(persons))]
        return persons