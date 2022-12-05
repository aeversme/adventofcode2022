def convert_to_stacks(input_list):
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
    procedures_list = []
    for procedure in input_list:
        procedure_split = procedure.split(' ')
        new_procedure = []
        for i in procedure_split:
            if i.isdigit():
                new_procedure.append(int(i))
        procedures_list.append(new_procedure)
    return procedures_list


def move_crates(crates, procedures):
    for procedure in procedures:
        # print(f'New procedure: moving {procedure[0]} from stack {procedure[1] - 1} ({len(crates[procedure[1] - 1])}'
        #       f' crates) to stack {procedure[2] - 1}')
        for i in range(procedure[0]):
            # print(f'   Moving crate {crates[procedure[1] - 1][-1]} from {crates[procedure[1] - 1]}')
            crate_to_move = crates[procedure[1] - 1].pop()
            crates[procedure[2] - 1].append(crate_to_move)
            # print(f'      Crate {crate_to_move} moved to {crates[procedure[2] - 1]}')
    return crates


def restack_crates(crate_list, procedure_list):
    stack_list = convert_to_stacks(crate_list)
    print(stack_list)
    procedure_list = convert_procedures(procedure_list)
    new_stacks = move_crates(stack_list, procedure_list)
    return new_stacks
