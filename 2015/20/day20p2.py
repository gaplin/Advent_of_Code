def get_present_count(N: int) -> int:
    result = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            first = i
            if first * 50 >= N:
                result += first * 11
            second = N // first
            if second != i and second * 50 >= N:
                result += second * 11
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