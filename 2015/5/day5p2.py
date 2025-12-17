import string

strings = open('input2.txt').read().splitlines()

def any_pair_at_least_two_times(text: str, pairs: list) -> bool:
    for pair in pairs:
        if text.count(pair) >= 2:
            return True
        
    return False

def any_repeating_char(text: str) -> bool:
    n = len(text)
    for i in range(2, n):
        if text[i] == text[i - 2]:
            return True
    
    return False

def nice_string(text: str, pairs: list) -> bool:
    return any_pair_at_least_two_times(text, pairs) and any_repeating_char(text)


all_pairs = [x + y for x in string.ascii_lowercase for y in string.ascii_lowercase]
result = 0
for candidate in strings:
    if nice_string(candidate, all_pairs) == True:
        result += 1

print(result)