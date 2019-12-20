# Read file and clean it

with open('input') as f:
    (wire1, wire2) = f.read().splitlines()
# Makes lists
wire1 = wire1.split(',')
wire2 = wire2.split(',')
# print(wire1)
# print(wire2)
# Tested with correct result
# wire1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
# wire2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
# wire1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# wire2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']


wire1_info = {
    'hLines': [],
    'vLines': [],
    'steps': 0,
    'last_steps': 0,
    'pos': [0, 0],
    'last_pos': [0, 0]
}

wire2_info = {
    'hLines': [],
    'vLines': [],
    'steps': 0,
    'last_steps': 0,
    'pos': [0, 0],
    'last_pos': [0, 0]
}

intersections = []


def split_input(_input):
    direction = _input[0]
    amount = int(_input[1:])
    return direction, amount


def move(_input, info):
    (direction, amount) = split_input(_input)
    info['last_steps'] = amount
    origin = info['pos']

    if direction == 'R':
        end = [info['pos'][0] + amount, info['pos'][1]]
        new_point = [origin, end]
        info['hLines'].append(new_point)
    if direction == 'L':
        end = [info['pos'][0] - amount, info['pos'][1]]
        new_point = [origin, end]
        info['hLines'].append(new_point)

    if direction == 'U':
        end = [info['pos'][0], info['pos'][1] + amount]
        info['vLines'].append([origin, end])
    if direction == 'D':
        end = [info['pos'][0], info['pos'][1] - amount]
        info['vLines'].append([origin, end])
    info['pos'] = end
    info['last_pos'] = origin


for instruct in wire1:
    move(instruct, wire1_info)
for instruct in wire2:
    move(instruct, wire2_info)


def check_intersect(info1, info2):
    for hLine in info1['hLines']:
        for vLine in info2['vLines']:
            if ((max(vLine[0][1], vLine[1][1]) >= hLine[0][1] >= min(vLine[0][1], vLine[1][1])) and
                    (max(hLine[0][0], hLine[1][0]) >= vLine[0][0] >= min(hLine[0][0], hLine[1][0]))):
                # check that point is not origin
                if vLine[0][0] != 0 and hLine[0][1] != 0:
                    intersections.append([vLine[0][0], hLine[0][1]])


check_intersect(wire1_info, wire2_info)
check_intersect(wire2_info, wire1_info)

answer = []
for s in intersections:
    answer.append(abs(s[0]) + abs(s[1]))

print(f"Manhattan distance: {min(answer)}")

wire1_info = {
    'hLines': [],
    'vLines': [],
    'steps': 0,
    'last_steps': 0,
    'pos': [0, 0],
    'last_pos': [0, 0]
}

wire2_info = {
    'hLines': [],
    'vLines': [],
    'steps': 0,
    'last_steps': 0,
    'pos': [0, 0],
    'last_pos': [0, 0]
}


def check_intersections(info):
    pos = info['pos']
    last_pos = info['last_pos']
    # last move made a vertical line
    if pos[0] == last_pos[0]:
        x = pos[0]
        ystart = min(pos[1], last_pos[1])
        yend = max(pos[1], last_pos[1])
        for sect in intersections:
            if sect[0] == x and (ystart <= sect[1] <= yend):
                steps_to_intersection = abs(sect[1] - last_pos[1])
                if f"{sect[0]}|{sect[1]}" not in intersectionsWithAmount:
                    intersectionsWithAmount[f"{sect[0]}|{sect[1]}"] = {'sect': sect,
                                                                       'amount': info['steps'] + steps_to_intersection}
                else:
                    intersectionsWithAmount[f"{sect[0]}|{sect[1]}"]['amount'] += info['steps'] + steps_to_intersection
    if pos[1] == last_pos[1]:
        y = pos[1]
        xstart = min(last_pos[0], pos[0])
        xend = max(last_pos[0], pos[0])
        for sect in intersections:
            if sect[1] == y and (xstart <= sect[0] <= xend):
                steps_to_intersection = abs(sect[0] - last_pos[0])
                if f"{sect[0]}|{sect[1]}" not in intersectionsWithAmount:
                    intersectionsWithAmount[f"{sect[0]}|{sect[1]}"] = {'sect': sect,
                                                                       'amount': info['steps'] + steps_to_intersection}
                else:
                    intersectionsWithAmount[f"{sect[0]}|{sect[1]}"]['amount'] += info['steps'] + steps_to_intersection


intersectionsWithAmount = {}

for instruction in wire1:
    move(instruction, wire1_info)
    check_intersections(wire1_info)
    wire1_info['steps'] += wire1_info['last_steps']

for instruction in wire2:
    move(instruction, wire2_info)
    check_intersections(wire2_info)
    wire2_info['steps'] += wire2_info['last_steps']

for key in intersectionsWithAmount:
    if 'steps' not in globals():
        steps = intersectionsWithAmount[key]['amount']
    else:
        if steps > intersectionsWithAmount[key]['amount']:
            steps = intersectionsWithAmount[key]['amount']

print(f'part 2 answer: {steps}')
