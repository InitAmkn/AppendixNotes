def choice(menu):
    for i in range(len(menu)):
        print(end="\t")
        for j in range(len(menu[i])):
            print(menu[i][j], end=' ')
        print()
    print()
    user_input = input()
    for i in menu:
        if user_input == i[0]:
            return user_input
    return choice(menu)


def input_note(menu):
    output_list = []
    for i in range(len(menu)):
        print(menu[i], end="\t")
        output_list.append(input())
    print()
    return output_list
