MIN_LETTER = 'a'
MIN_DIGIT = '1'

X_DIRECTION_TO_MOVE = {
    1: "R",
    -1: "L",
}
Y_DIRECTION_TO_MOVE = {
    1: "U",
    -1: "D",
}


def get_cell_coords(cell: str):
    letter = cell[0]
    digit = cell[1]
    return [ord(letter) - ord(MIN_LETTER), ord(digit) - ord(MIN_DIGIT)]


def get_direction(x, y):
    if y > x:
        return 1
    elif y < x:
        return -1
    else:
        return 0


current_cell = input()
destination_cell = input()

current_point = get_cell_coords(current_cell)
destination_point = get_cell_coords(destination_cell)


moves = []
moves_count = 0

while current_point != destination_point:
    move = ""
    x_direction = get_direction(current_point[0], destination_point[0])
    if x_direction:
        move += X_DIRECTION_TO_MOVE[x_direction]
        current_point[0] += x_direction
    y_direction = get_direction(current_point[1], destination_point[1])
    if y_direction:
        move += Y_DIRECTION_TO_MOVE[y_direction]
        current_point[1] += y_direction
    moves.append(move)
    moves_count += 1

print(moves_count)
for move in moves:
    print(move)
