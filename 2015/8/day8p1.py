def normal_length(text: str) -> int:
    result = 0
    n = len(text)
    i = 1
    while i < n - 1:
        if text[i] == '\\':
            if text[i + 1] in '"\\':
                i += 2
            else:
                i += 4
            result += 1
            continue
        i += 1
        result += 1

    return result

input = open('input2.txt').read().splitlines()

literals, memory = 0, 0
for line in input:
    length = len(line)
    mem = normal_length(line)
    literals += length
    memory += mem

print(literals - memory)