moves = open('input2.txt').read().strip()

directions = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

current_positions = ([0, 0], [0, 0])
visited_places = {(0, 0)}

for idx, move in enumerate(moves):
    direction = directions[move]
    current_positions[idx % 2][0] += direction[0]
    current_positions[idx % 2][1] += direction[1]
    visited_places.add(tuple(current_positions[idx % 2]))

print(len(visited_places))