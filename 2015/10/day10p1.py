def step(sequence: list) -> list:
    current_value = None
    current_count = 0
    result = []
    for char in sequence:
        if char == current_value:
            current_count += 1
        else:
            if current_value != None:
                result += [str(current_count), current_value]
            current_value = char
            current_count = 1
    else:
        result += [str(current_count), current_value]

    return result

seq = [x for x in open('input2.txt').read().strip()]
for _ in range(40):
    seq = step(seq)

print(len(seq))
