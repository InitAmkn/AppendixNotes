import src.menu.request as request
import src.menu.menu_ as menu


def start():
    list_input = []
    list_input.append(request.choice(menu.action))
    list_input.append(request.input_note(menu.note))
    return list_input
