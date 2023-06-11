def choice(menu):
    for i in range(len(menu)-1):
        print(end="\t")
        for j in range(len(menu[i])):
            print(menu[i][j], end=' ')
        print()
    print()
    user_input = input()
    for i in range(len(menu)-1):
        if user_input == menu[i][0]:
            return user_input
    print(menu[len(menu)-1][1])
    return choice(menu)


def input_note(menu):
    output_list = []
    for i in range(len(menu)):
        print(menu[i], end="\t")
        data_input = input()
        if data_input == "":
            return input_note(menu)
        output_list.append(data_input)
    print()
    return output_list


def input_date(menu):
    print(menu[0], end="\t")
    output = input()
    output_list = output.split(".")
    if len(output_list) != 3:
        print(menu[1])
        return input_date(menu)
    for i in output_list:
        if i.isdigit() == False:
            print(menu[1])
            return input_date(menu)
    print()
    return output_list


def input_index(menu):
    print(menu[0], end="\t")
    output = input()
    if output.isdigit() == False:
        print(menu[1])
        return input_index(menu)
    print()
    return int(output)
