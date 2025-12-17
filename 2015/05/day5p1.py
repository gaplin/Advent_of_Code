strings = open('input2.txt').read().splitlines()

def count_vowels(text: str) -> int:
    vowels = 'aeiou'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    
    return count

def letter_twice_in_a_row(text: str) -> bool:
    n = len(text)
    for i in range(1, n):
        if text[i] == text[i - 1]:
            return True
    
    return False

def does_not_contain(text: str, prohibited_strings: list) -> bool:
    for prohibited_string in prohibited_strings:
        if prohibited_string in text:
            return False

    return True

def nice_string(text: str) -> bool:
    vowels_count = count_vowels(text)
    if vowels_count < 3:
        return False
    
    any_letter_twice_in_a_row = letter_twice_in_a_row(text)
    if any_letter_twice_in_a_row == False:
        return False
    
    prohibited_strings = ['ab', 'cd', 'pq', 'xy']
    without_prohibited_strings = does_not_contain(text, prohibited_strings)
    if without_prohibited_strings == False:
        return False

    return True

result = 0

for string in strings:
    if nice_string(string) == True:
        result += 1

print(result)