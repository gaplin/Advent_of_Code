moves = open('input2.txt').read().strip()

directions = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

current_position = [0, 0]
visited_places = {(0, 0)}

for move in moves:
    direction = directions[move]
    current_position[0] += direction[0]
    current_position[1] += direction[1]
    visited_places.add(tuple(current_position))

print(len(visited_places))