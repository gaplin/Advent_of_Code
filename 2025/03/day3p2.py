lines = open('input2.txt').read().splitlines()

def getmax(nums: list[int], n: int, idx: int, remaining: int, cache: dict) -> int:
    if idx == -1 or remaining == 0:
        return 0
    
    key = (idx, remaining)
    if key in cache:
        return cache[key]
    num = nums[idx]
    result = max(
        getmax(nums, n, idx - 1, remaining - 1, cache) * 10 + num,
        getmax(nums, n, idx - 1, remaining, cache)
    )
    cache[key] = result
    return result

result = 0
for line in lines:
    all_nums = [int(x) for x in line]
    n = len(all_nums)
    result += getmax(all_nums, n, n - 1, 12, {})

print(result)