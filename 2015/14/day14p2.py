import re

input = open('input2.txt').read().splitlines()
reindeers = []
for line in input:
    reindeers.append(tuple(map(int, re.findall(r'\d+', line))))

target = 2503
distances = [0 for _ in reindeers]
points = [0 for _ in reindeers]
n = len(points)
for i in range(1, target + 1):
    for idx, (speed, travel_time, rest_time) in enumerate(reindeers):
        cycle_length = (travel_time + rest_time)
        cycle_distance = speed * travel_time
        full_cycles = i // cycle_length
        remaining_time = i % cycle_length
        distance = full_cycles * cycle_distance + min(remaining_time, travel_time) * speed
        distances[idx] = distance
    
    val_idxes = [(distance, idx) for idx, distance in enumerate(distances)]
    val_idxes.sort(reverse=True)
    current_max = val_idxes[0][0]
    j = 0
    while j < n and val_idxes[j][0] == current_max:
        points[val_idxes[j][1]] += 1
        j += 1

result = max(points)
print(result)