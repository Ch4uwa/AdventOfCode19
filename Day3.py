# Read file and clean it
with open('input') as f:
    data = f.readlines()


def clean_data(in_data):
    temp = ''
    out_data = []
    for i in in_data:
        temp = temp + i
        if i == ',':
            out_data.append(temp.strip(','))
            temp = ''
        if i == '\n':
            out_data.append(temp.strip('\n'))
            temp = ''
    print('clean func has run')
    return out_data


def coord(values):
    coords = [(500, 500)]
    x = 500
    y = 500
    scaling = 0.05
    for i in values:
        if i[0] == 'R':
            x += (scaling * float(i[1:]))
        if i[0] == 'U':
            y -= (scaling * float(i[1:]))
        if i[0] == 'L':
            x -= (scaling * float(i[1:]))
        if i[0] == 'D':
            y += (scaling * float(i[1:]))
        coords.append((x, y))
    print('coord func have been run')
    return coords
