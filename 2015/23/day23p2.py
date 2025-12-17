def hlf(program, r):
    program[0][r] >>= 1

def tpl(program, r):
    program[0][r] *= 3

def inc(program, r):
    program[0][r] += 1

def jmp(program, offset):
    program[1] += offset

def jie(program, r, offset) -> bool:
    if program[0][r] % 2 == 0:
        program[1] += offset
        return True
    return False

def jio(program, r, offset) -> bool:
    if program[0][r] == 1:
        program[1] += offset
        return True
    return False

def play(program: list):
    #program = [registers, ip, instructions]
    instructions = program[2]
    n = len(instructions)
    while 0 <= program[1] < n:
        code, args = instructions[program[1]]
        if code == 'hlf':
            hlf(program, *args)
        elif code == 'tpl':
            tpl(program, *args)
        elif code == 'inc':
            inc(program, *args)
        elif code == 'jmp':
            jmp(program, *args)
            continue
        elif code == 'jie':
            if jie(program, *args):
                continue
        elif code == 'jio':
            if jio(program, *args):
                continue
        program[1] += 1

input = open('input2.txt').read().splitlines()
instructions = []
for line in input:
    code, args = line.split(' ', 1)
    args = args.split(', ')
    if code == 'jmp':
        args[0] = int(args[0])
    elif len(args) == 2:
        args[1] = int(args[1])
    instructions.append((code, tuple(args)))

registers = {'a': 1, 'b': 0}
program = [registers, 0, instructions]
play(program)
print(registers['b'])