ticker_tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

aunts = []
input = open('input2.txt').read().splitlines()

for line in input:
    line = line.split(': ', 1)[1]
    aunt = {}
    attributs = line.split(', ')
    for attr in attributs:
        key, value = attr.split(': ')
        aunt[key] = int(value)
    aunts.append(aunt)

result = 0
n = len(aunts)
for i in range(n):
    valid_aunt = True
    for key, value in aunts[i].items():
        if key not in ticker_tape or ticker_tape[key] != value:
            valid_aunt = False
            break
    if valid_aunt == True:
        result = i + 1
        break

print(result)