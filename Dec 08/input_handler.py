def extract_procedure(input_list):
    list1 = []
    list2 = []
    is_list2 = False
    for item in input_list:
        if item == '':
            is_list2 = True
        elif item != '' and not is_list2:
            list1.append(item)
        else:
            list2.append(item)
    return list1, list2


def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    list1, list2 = extract_procedure(data_strip)
    return list1, list2
