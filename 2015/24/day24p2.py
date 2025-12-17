from heapq import heappop, heappush

def get_key(nums: list) -> tuple:
    return tuple(sorted(nums))

def BFS(target: int, all_nums: list) -> int:
    Q = [(0, 1, target, [])]
    visited = {()}

    while Q:
        length, qe, remaining_part, nums = heappop(Q)
        if remaining_part == 0:
            return qe
        
        for num in all_nums:
            if num in nums or num > remaining_part:
                continue
            new_nums = nums + [num]
            key = get_key(new_nums)
            if key not in visited:
                visited.add(key)
                heappush(Q, (length + 1, qe * num, remaining_part - num, new_nums))

    raise Exception('target not found')

nums = [int(x) for x in open('input2.txt').read().splitlines()]
S = sum(nums) // 4
res = BFS(S, nums)
print(res)