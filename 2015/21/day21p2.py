from math import ceil

def win(player, boss) -> bool:
    player_damage = max(1, player[1] - boss[2])
    boss_damage = max(1, boss[1] - player[2])

    player_HP = player[0]
    boss_HP = boss[0]

    player_turns = ceil(boss_HP / player_damage)
    boss_turns = ceil(player_HP / boss_damage)

    return player_turns <= boss_turns

input = open('input2.txt').read().splitlines()
weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
    ]

armor = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]

rings = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]

boss = []
for line in input:
    boss.append(int(line.split(': ')[-1]))

n_w = len(weapons)
n_a = len(armor)
n_r = len(rings)

result = 0
for w_id in range(n_w):
    for a_id in range(n_a):
        for r1_id in range(n_r - 1):
            for r2_id in range(r1_id + 1, n_r):
                cost = weapons[w_id][0] + armor[a_id][0] + rings[r1_id][0] + rings[r2_id][0]
                player = [100, 0, 0]
                for i in range(1, 3):
                    player[i] = weapons[w_id][i] + armor[a_id][i] + rings[r1_id][i] + rings[r2_id][i]
                if win(player, boss) == False:
                    result = max(result, cost)

print(result)