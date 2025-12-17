def get_key(nums: list) -> tuple:
    return tuple(sorted(nums))

def dfs(target: int, nums: list, taken_nums: list, visited: set) -> int:
    key = get_key(taken_nums)
    visited.add(key)

    if target == 0:
        return 1
    result = 0
    for i in range(len(nums)):
        if i in taken_nums or nums[i] > target:
            continue
        new_taken_nums = taken_nums + [i]
        new_key = get_key(new_taken_nums)
        if new_key not in visited:
            result += dfs(target - nums[i], nums, new_taken_nums, visited)

    return result

nums = [int(x) for x in open('input2.txt').read().splitlines()]
target = 150
result = dfs(target, nums, [], set())
print(result)