input = open('input2.txt').read().splitlines()

literals, encoded = 0, 0
for line in input:
    length = len(line)
    literals += length
    encoded += length + line.count('\\') + line.count('"') + 2

print(encoded - literals)