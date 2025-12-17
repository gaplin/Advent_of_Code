def get_list_sum(l: list, prohibited_key: str) -> int:
    result = 0
    for value in l:
        if type(value) == dict:
            result += get_dict_sum(value, prohibited_key)
        elif type(value) == int:
            result += value
        elif type(value) == list:
            result += get_list_sum(value, prohibited_key)

    return result

def get_dict_sum(d: dict, prohibited_key: str) -> int:
    if prohibited_key in d.values():
        return 0
    result = 0
    for value in d.values():
        if type(value) == dict:
            result += get_dict_sum(value, prohibited_key)
        elif type(value) == int:
            result += value
        elif type(value) == list:
            result += get_list_sum(value, prohibited_key)

    return result
            
input = open('input2.txt').read().strip()
d = eval(input)
result = get_dict_sum(d, 'red')

print(result)