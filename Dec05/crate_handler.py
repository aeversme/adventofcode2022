def convert_to_stacks(input_list):
    """
    Takes a list of strings with [ and ] characters and returns a 2D list array of 'crates.'
    :param input_list: list
    :return: list
    """
    stacks = []
    stack_count = int(input_list.pop()[-1])
    for _ in range(stack_count):
        stacks.append([])

    space_count = 0
    current_stack = 0
    for input_string in input_list:
        for char in input_string:
            if not char.isalpha() and char == ' ':
                space_count += 1
            elif not char.isalpha():
                if space_count > 7:
                    current_stack += 2
                elif space_count > 2:
                    current_stack += 1
                space_count = 0
            else:
                stacks[current_stack].append(char)
                current_stack += 1
        space_count = 0
        current_stack = 0

    for stack in stacks:
        stack.reverse()

    return stacks


def convert_procedures(input_list):
    """
    Takes a list of strings and returns a 2D list array of 'procedures.'
    :param input_list: list
    :return: list
    """
    procedures_list = []
    for procedure in input_list:
        procedure_split = procedure.split(' ')
        new_procedure = []
        for i in procedure_split:
            if i.isdigit():
                new_procedure.append(int(i))
        procedures_list.append(new_procedure)
    return procedures_list


def move_crates(crates, procedures, crane9001=False):
    """
    Takes a 2D list array of 'crates' and a 2D list array of 'procedures' and an optional Boolean, and returns a 2D
    list array of moved 'crates.'
    :param crates: list
    :param procedures: list
    :param crane9001:Boolean
    :return:list
    """
    for procedure in procedures:
        if crane9001:
            # print(f'Procedure: {procedure}')
            # print(f'Moving {procedure[0]} crates from {procedure[1]}: {crates[procedure[1] - 1]}')
            crates_to_move = crates[procedure[1] - 1][-procedure[0]:]
            # print(f'   Moving crates: {crates_to_move}')
            for crate in crates_to_move:
                crates[procedure[2] - 1].append(crate)
                crates[procedure[1] - 1].pop()
        else:
            for i in range(procedure[0]):
                crate_to_move = crates[procedure[1] - 1].pop()
                crates[procedure[2] - 1].append(crate_to_move)
        # print(crates)
    return crates


def restack_crates(crate_list, procedure_list, part_two=False):
    """
    Takes two lists of strings and an optional Boolean, and returns a 2D list array.
    :param crate_list: list
    :param procedure_list: list
    :param part_two: Boolean
    :return: list
    """
    crane9001 = False
    if part_two:
        crane9001 = True
    stack_list = convert_to_stacks(crate_list)
    print(stack_list)
    procedure_list = convert_procedures(procedure_list)
    new_stacks = move_crates(stack_list, procedure_list, crane9001)
    return new_stacks
