def convert_input(data):
    data_strip = [i.strip('\n') for i in data]
    converted_data = []
    for item in data_strip:
        item_split = item.split(',')
        converted_data.append(item_split)
    return converted_data
