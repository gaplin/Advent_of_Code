lines = open('input2.txt').read().splitlines()

position = 50
circle_size = 100
result = 0
for rotation in lines:
    direction, steps = rotation[0], int(rotation[1:])
    result += steps // circle_size
    steps %= circle_size
    if direction == 'L':
        steps *= -1

    if position != 0 and (position + steps <= 0 or position + steps >= 100):
        result += 1

    position = (position + steps) % circle_size
 
print(result)