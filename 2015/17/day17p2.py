def get_key(nums: list) -> tuple:
    return tuple(sorted(nums))

def dfs(target: int, nums: list, taken_nums: list, visited: set) -> list:
    key = get_key(taken_nums)
    visited.add(key)

    if target == 0:
        return [taken_nums]
    
    result = []
    for i in range(len(nums)):
        if i in taken_nums or nums[i] > target:
            continue
        new_taken_nums = taken_nums + [i]
        new_key = get_key(new_taken_nums)
        if new_key not in visited:
            child_result = dfs(target - nums[i], nums, new_taken_nums, visited)
            for res in child_result:
                result.append(res)

    return result

nums = [int(x) for x in open('input2.txt').read().splitlines()]
target = 150
results = dfs(target, nums, [], set())
results.sort(key=lambda x: len(x))
current_min = len(results[0])
count = 0
n = len(results)
for i in range(n):
    if len(results[i]) != current_min:
        break
    count += 1
print(count)