def get_length(num: int) -> int:
    length = 1
    while num >= 10:
        num /= 10
        length += 1

    return length

def is_repeated(text: str, block_size: int, n: int) -> bool:
    if block_size > n // 2 or n % block_size != 0:
        return False
    for i in range(block_size, n):
        if text[i] != text[i % block_size]:
            return False
        
    return True

def is_invalid(num: int) -> bool:
    str_num = str(num)
    n = len(str_num)
    if n == 1:
        return False
    
    for l in range(1, n // 2 + 1):
        if is_repeated(str_num, l, n) == True:
            return True
        
    return False

def sum_invalid_in_range(l: int, r: int) -> int:
    result = 0

    while l <= r:
        if is_invalid(l) == True:
            result += l
        l += 1
    
    return result

line = open('input2.txt').read().strip()
ranges = line.split(',')

result = 0
for ran in ranges:
    first, second = ran.split('-')
    first, second = int(first), int(second)
    assert first <= second
    result += sum_invalid_in_range(first, second)

print(result)