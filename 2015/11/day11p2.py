import string

def next_text(current: str, prohibited: set()) -> str:
    a = ord('a')
    z = ord('z')
    res_list = []
    i = len(current) - 1
    while i >= 0:
        cur = ord(current[i])
        while True:
            cur += 1
            if cur > z:
                cur = a
                break
            if cur not in prohibited:
                break
        
        res_list.append(chr(cur))
        if cur != a:
            break
        i -= 1
    
    if i == -1:
        return None
    i -= 1
    while i >= 0:
        res_list.append(current[i])
        i -= 1
    
    return ''.join(reversed(res_list))

def increasing_straight(text: str) -> bool:
    n = len(text)
    for i in range(2, n):
        if ord(text[i]) - 2 == ord(text[i - 1]) - 1 == ord(text[i - 2]):
            return True
        
    return False

def two_different_pairs(text: str) -> bool:
    counts = 0
    for a in string.ascii_lowercase:
        if a * 2 in text:
            counts += 1
            if counts == 2:
                return True
            
    return False

first = open('input2.txt').read().strip()
prohibited = {ord('i'), ord('l'), ord('o')}
result = ''
count = 2
while first != None:
    if increasing_straight(first) == True and two_different_pairs(first) == True:
        count -= 1
        if count == 0:
            result = first
            break
    first = next_text(first, prohibited)

print(first)