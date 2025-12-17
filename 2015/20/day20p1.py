def get_present_count(N: int) -> int:
    result = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            first = i
            second = N // first
            result += first * 10
            if second != i:
                result += second * 10
        i += 1

    return result

target = int(open('input2.txt').read().strip())
i = 1
while True:
    presents = get_present_count(i)
    if presents >= target:
        break
    i += 1

print(i)