braces = open('input2.txt').read().strip()

level = 0
for idx, char in enumerate(braces):
    if char == '(':
        level += 1
    else:
        level -= 1
    if level == -1:
        result = idx + 1
        break

print(result)