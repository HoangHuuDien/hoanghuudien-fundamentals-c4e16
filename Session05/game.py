map_sokoban = {
    "x" : 5,
    "y" : 5,
}

player = {
    "x" : 0,
    "y" : 4
}

boxes = [
    {"x" : 1, "y" : 1},
    {"x" : 2, "y" : 2},
    {"x" : 3, "y" : 3},
]



for y in range(map_sokoban['y']):
    for x in range(map_sokoban['x']):

        box_is_here = False
        for box in boxes:
            if box['x'] == x and box['y'] == y:
                print('B ', end='')
                box_is_here = True

        if x == player["x"] and y == player["y"]:
            print('P ', end='')
        elif box_is_here is not True:
            print('- ', end='')
    print()
