import sys

with open(sys.argv[1], 'r') as file:
    program = [line.rstrip() for line in file]

crt = [
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']
]

x = 1
cycle = 1
ri = 0
pi = 0

def draw():
    global x
    global cycle
    global ri
    global pi
        
    if abs(x - pi) < 2:
        crt[ri][pi] = '#'
    else:
        crt[ri][pi] = '.'

    if cycle % 240 == 0:
        ri, pi = 0, 0
    elif cycle % 40 == 0:
        ri, pi = ri+1, 0
    else:
        pi += 1

for instruction in program:
    draw()
    if instruction.startswith('noop'):
        cycle += 1
    else:
        cycle += 1
        draw()
        cycle += 1
        x += int(instruction[5:])

for row in crt:
    print("".join(row))
