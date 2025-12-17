from heapq import heappop, heappush

def apply_effects(player: list, boss: list, effects: list):
    if effects[0] > 0:
        player[1] = 7
        effects[0] -= 1
    if effects[1] > 0:
        boss[0] -= 3
        effects[1] -= 1
    if effects[2] > 0:
        player[2] += 101
        effects[2] -= 1
    
def make_a_turn(player: list, boss: list, effects: list) -> None:
    apply_effects(player, boss, effects)
    if boss[0] <= 0:
        boss[0] == 0
        return
    player[0] -= max(1, boss[1] - player[1])
    if player[0] <= 0:
        player[0] = 0
        return
    apply_effects(player, boss, effects)

def BFS(player: tuple, boss: tuple, spells: list) -> int:
    initial_state = ((player, boss, (0, 0, 0)))
    Q = [(0, initial_state)]
    distances = {initial_state: 0}
    while Q:
        distance, u = heappop(Q)
        if u[1][0] == 0:
            return distance
        
        if u[0][0] == 1:
            continue

        for spell in spells:
            player = [u[0][0] - 1, 0, u[0][1]]
            boss = list(u[1])
            effects = list(u[2])
            if spell[0](player, boss, effects) == False:
                continue
            spell[1](player, boss, effects)
            make_a_turn(player, boss, effects)
            if player[0] == 0:
                continue
            new_state = ((player[0], player[2]), tuple(boss), tuple(effects))
            new_distance = distance + spell[2]
            if new_state not in distances or distances[new_state] > new_distance:
                distances[new_state] = new_distance
                heappush(Q, (new_distance, new_state))

    raise Exception('Winning state not found')

def can_apply_missle(player, boss, effects):
    return player[2] >= 53
def apply_missle(player, boss, effects):
    boss[0] -= 4
    player[2] -= 53

def can_apply_drain(player, boss, effects):
    return player[2] >= 73
def apply_drain(player, boss, effects):
    boss[0] -= 2
    player[0] += 2
    player[2] -= 73

def can_apply_shield(player, boss, effects):
    return player[2] >= 113 and effects[0] == 0
def apply_shield(player, boss, effects):
    effects[0] = 6
    player[2] -= 113

def can_apply_poison(player, boss, effects):
    return player[2] >= 173 and effects[1] == 0
def apply_poison(player, boss, effects):
    effects[1] = 6
    player[2] -= 173

def can_apply_recharge(player, boss, effects):
    return player[2] >= 229 and effects[2] == 0
def apply_recharge(player, boss, effects):
    effects[2] = 5
    player[2] -= 229

spells = [
    (
        can_apply_missle,
        apply_missle,
        53
    ),
    (
        can_apply_drain,
        apply_drain,
        73
    ),
    (
        can_apply_shield,
        apply_shield,
        113
    ),
    (
        can_apply_poison,
        apply_poison,
        173
    ),
    (
        can_apply_recharge,
        apply_recharge,
        229
    )
]
input = open('input2.txt').read().splitlines()  
boss = []
for line in input:
    boss.append(int(line.split(' ')[-1]))

player = (50, 500)
boss = tuple(boss)
result = BFS(player, boss, spells)
print(result)