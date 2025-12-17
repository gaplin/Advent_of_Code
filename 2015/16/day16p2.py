ticker_tape = {
    'children': lambda x: x == 3,
    'cats': lambda x: x > 7,
    'samoyeds': lambda x: x == 2,
    'pomeranians': lambda x: x < 3,
    'akitas': lambda x: x == 0,
    'vizslas': lambda x: x == 0,
    'goldfish': lambda x: x < 5,
    'trees': lambda x: x > 3,
    'cars': lambda x: x == 2,
    'perfumes': lambda x: x == 1
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
        if key not in ticker_tape or ticker_tape[key](value) == False:
            valid_aunt = False
            break
    if valid_aunt == True:
        result = i + 1
        break

print(result)