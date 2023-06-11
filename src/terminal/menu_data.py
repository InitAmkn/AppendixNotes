import datetime
action = [('', 'Select an action:'),
          ('1', 'Add'),
          ('2', 'Read all notes'),
          ('3', 'Edit note'),
          ('4', 'Show by date'),
          ('5', 'Delete by index'),
          ('', 'Incorrect choice of action')
          ]

add_note = ["Enter the title of the note:",
            "Enter the body of the note:"]

enter_date = [
    f"Enter the date, Example: {datetime.datetime.now().day}.{datetime.datetime.now().month}.{datetime.datetime.now().year} :",
    "Incorrect date entry"]

enter_index = [
    "Enter the index:",
    "Incorrect index"]
