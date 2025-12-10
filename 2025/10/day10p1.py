def lights_to_bits(lights: str) -> int:
    mask = 1
    result = 0
    for c in lights:
        if c == '#':
            result |= mask
        mask <<= 1
    return result

def button_to_bits(button: tuple) -> int:
    result = 0
    for num in button:
        result |= (1 << num)
    return result

def get_min_ops(target: int, buttons: list[int]) -> int:
    result = len(buttons)
    limit = (1 << len(buttons))
    for i in range(0, limit):
        current_state = 0
        mask = 1
        buttons_pressed = 0
        for button in buttons:
            if (i & mask) != 0:
                current_state ^= button
                buttons_pressed += 1
            mask <<= 1
        if current_state == target:
            result = min(result, buttons_pressed)

    return result

lines = open('input2.txt').read().splitlines()

result = 0
for line in lines:
    words = line.split()
    light = words[0][1:-1]
    light_bits = lights_to_bits(light)

    buttons = [tuple(map(int, x[1:-1].split(','))) for x in words[1:-1]]
    buttons_bits = [button_to_bits(x) for x in buttons]

    result += get_min_ops(light_bits, buttons_bits)

print(result)