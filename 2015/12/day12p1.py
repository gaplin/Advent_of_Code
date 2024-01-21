import re

input = open('input2.txt').read().strip()

result = sum([int(x) for x in re.findall(r'[0-9-]+', input)])

print(result)