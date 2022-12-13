def convert_input(calorie_data):
    calorie_strip = [i.strip('\n') for i in calorie_data]
    for i in range(len(calorie_strip)):
        if calorie_strip[i] != '':
            calorie_strip[i] = int(calorie_strip[i])
    return calorie_strip
