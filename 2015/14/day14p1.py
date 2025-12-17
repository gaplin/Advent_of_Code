import re

input = open('input2.txt').read().splitlines()
reindeers = []
for line in input:
    reindeers.append(tuple(map(int, re.findall(r'\d+', line))))

target = 2503
distances = []
for speed, travel_time, rest_time in reindeers:
    cycle_length = (travel_time + rest_time)
    cycle_distance = speed * travel_time
    full_cycles = target // cycle_length
    remaining_time = target % cycle_length
    distance = full_cycles * cycle_distance + min(remaining_time, travel_time) * speed
    distances.append(distance)

result = max(distances)
print(result)