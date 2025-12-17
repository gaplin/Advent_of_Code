lines = open('input2.txt').read().splitlines()

result = 0
for line in lines:
    max_num = -1
    max_jolt = 0
    for num in map(int, line):
        max_jolt = max(max_jolt, max_num * 10 + num)
        max_num = max(max_num, num)

    result += max_jolt

print(result)    