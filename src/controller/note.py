from datetime import datetime


class Note(object):
    """description of the note"""

    def __init__(self, heading="", body="", date_of_creation=""):
        """note properties"""
        self.heading = heading
        self.body = body
        if date_of_creation == "":
            self.date_of_creation = datetime.now()
        else:
            self.date_of_creation = datetime.strptime(
                date_of_creation, "%Y-%m-%d %H:%M:%S.%f")

    def __str__(self):
        return f' Head: {self.heading}\n\
 Body: {self.body}\n\
 Date: {self.date_of_creation.strftime("%d.%m.%Y %H:%M:%S")}'
