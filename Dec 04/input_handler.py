def convert_to_sets(set_list):
    sets = []
    for string_set in set_list:
        string_set_split = string_set.split('-')
        new_set = set(range(int(string_set_split[0]), int(string_set_split[1]) + 1))
        sets.append(new_set)
    return sets


def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    converted_data = []
    for item in data_strip:
        item_split = item.split(',')
        item_set = convert_to_sets(item_split)
        converted_data.append(item_set)
    return converted_data
