import datetime


class Note(object):
    """description of the note"""

    def __init__(self, heading="", body=""):
        """note properties"""
        self.heading = heading
        self.body = body
        self.date_of_creation = datetime.datetime.now()

    def __str__(self):
        return f"{self.heading} {self.body} {self.date_of_creation}"
