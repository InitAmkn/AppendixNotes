import src.controller.note as note


class Notes_collection(object):

    def __init__(self, all_notes={}):
        self.all_notes = {}
        self.all_notes = all_notes
        self.index = 1

    def create_new_note(self, heading, body):
        self.all_notes[self.index] = note.Note(heading, body)
        self.index = self.index+1

    def __str__(self):
        lst = []
        for i in self.all_notes:
            lst.append(f"{i} - {self.all_notes[i]}")
        return "\n".join(lst)

    def edit_note(self, heading, body, index):
        for i in self.all_notes:
            if i == index:
                self.all_notes[index] = note.Note(heading, body)
                return True
        return False

    def show_by_date(self, day=""):
        day_list = day.split(".")
        lst = []
        print(day_list)
        for i in self.all_notes:
            if f"{self.all_notes[i].date_of_creation.day}" == day_list[0]:
                if f"{self.all_notes[i].date_of_creation.month}" == day_list[1]:
                    if f"{self.all_notes[i].date_of_creation.year}" == day_list[2]:
                        lst.append(f"{i} - {self.all_notes[i]}")
        return "\n".join(lst)

    def delete_by_index(self, index):
        for i in self.all_notes:
            if i == index:
                return self.all_notes.pop(index)
        return False
