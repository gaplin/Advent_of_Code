lines = open('input2.txt').read().splitlines()

position = 50
circle_size = 100
result = 0
for rotation in lines:
    direction, steps = rotation[0], int(rotation[1:])
    if direction == 'L':
        steps *= -1

    position = (position + steps) % circle_size
    if position == 0:
        result += 1
 
print(result)