def get_length(num: int) -> int:
    length = 1
    while num >= 10:
        num /= 10
        length += 1

    return length

def is_invalid(num: int) -> bool:
    length = get_length(num)
    if length % 2 == 1:
        return False
    half = length // 2
    mod = 10 ** half
    left, right = num // mod, num % mod
    return left == right

def sum_invalid_in_range(l: int, r: int) -> int:
    result = 0

    while l <= r:
        if is_invalid(l):
            result += l
        l += 1
    
    return result

line = open('input2.txt').read().strip()
ranges = line.split(',')

result = 0
for range in ranges:
    first, second = range.split('-')
    first, second = int(first), int(second)
    assert first <= second
    result += sum_invalid_in_range(first, second)

print(result)