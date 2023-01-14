import sys
from blessed import Terminal
from time import sleep

with open(sys.argv[1], 'r') as file:
    program = [line.rstrip() for line in file]

crt = [['.'] * 40 for _ in range(6)]
x = 1 # register x
cycle = 1
ri = 0 # crt row index (y)
pi = 0 # crt pixel index (x)

term = Terminal()

def clearSprite(x):
    global ri
    global term

    sx = x-1
    if sx >= 0 and sx <= 39:
        print(term.move_yx(ri, sx) + crt[ri][sx])

    sx = x
    if sx >= 0 and sx <= 39:
        print(term.move_yx(ri, sx) + crt[ri][sx])

    sx = x+1
    if sx >= 0 and sx <= 39:
        print(term.move_yx(ri, sx) + crt[ri][sx])
    
def drawSprite(x):
    global ri
    global term

    sx = x-1
    if sx >= 0 and sx <= 39:
        print(term.move_yx(ri, sx) + term.bold_green('#'))

    sx = x
    if sx >= 0 and sx <= 39:
        print(term.move_yx(ri, sx) + term.bold_green('#'))

    sx = x+1
    if sx >= 0 and sx <= 39:
        print(term.move_yx(ri, sx) + term.bold_green('#'))

def updateCrt():
    global x
    global cycle
    global ri
    global pi
    global term

    sleep(0.05)
    
    if abs(x - pi) < 2:
        crt[ri][pi] = '#'
        print(term.move_yx(ri, pi) + '#')

    if cycle % 240 == 0:
        clearSprite(x)
        ri, pi = 0, 0
    elif cycle % 40 == 0:
        clearSprite(x)
        ri, pi = ri+1, 0
    else:
        pi += 1

def greenScanLine(x):
    print(term.move_yx(0, x) + term.bold_on_green(crt[0][x]))
    print(term.move_yx(1, x) + term.bold_on_green(crt[1][x]))
    print(term.move_yx(2, x) + term.bold_on_green(crt[2][x]))
    print(term.move_yx(3, x) + term.bold_on_green(crt[3][x]))
    print(term.move_yx(4, x) + term.bold_on_green(crt[4][x]))
    print(term.move_yx(5, x) + term.bold_on_green(crt[5][x]))

def clearScanLine(x):
    print(term.move_yx(0, x) + crt[0][x])
    print(term.move_yx(1, x) + crt[1][x])
    print(term.move_yx(2, x) + crt[2][x])
    print(term.move_yx(3, x) + crt[3][x])
    print(term.move_yx(4, x) + crt[4][x])
    print(term.move_yx(5, x) + crt[5][x])

def letterRecognition(start, end):
    slice = [crt[i][start:end] for i in range(6)]
    a = [
        [".","#","#","."],
        ["#",".",".","#"],
        ["#",".",".","#"],
        ["#","#","#","#"],
        ["#",".",".","#"],
        ["#",".",".","#"]
    ]
    b = [
        ["#","#","#","."],
        ["#",".",".","#"],
        ["#","#","#","."],
        ["#",".",".","#"],
        ["#",".",".","#"],
        ["#","#","#","."]
    ]
    e = [
        ["#","#","#","#"],
        ["#",".",".","."],
        ["#","#","#","."],
        ["#",".",".","."],
        ["#",".",".","."],
        ["#","#","#","#"]
    ]
    h = [
        ["#",".",".","#"],
        ["#",".",".","#"],
        ["#","#","#","#"],
        ["#",".",".","#"],
        ["#",".",".","#"],
        ["#",".",".","#"]
    ]
    k = [
        ["#",".",".","#"],
        ["#",".","#","."],
        ["#","#",".","."],
        ["#",".","#","."],
        ["#",".","#","."],
        ["#",".",".","#"]
    ]
    r = [
        ["#","#","#","."],
        ["#",".",".","#"],
        ["#",".",".","#"],
        ["#","#","#","."],
        ["#",".","#","."],
        ["#",".",".","#"]
    ]
    u = [
        ["#",".",".","#"],
        ["#",".",".","#"],
        ["#",".",".","#"],
        ["#",".",".","#"],
        ["#",".",".","#"],
        [".","#","#","."]
    ]

    if a == slice:
        return "A"
    elif b == slice:
        return "B"
    elif e == slice:
        return "E"
    elif h == slice:
        return "H"
    elif k == slice:
        return "K"
    elif r == slice:
        return "R"
    elif u == slice:
        return "U"
    else:
        return None

with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    for row in crt:
        print("".join(row))

    drawSprite(x)

    for instruction in program:
        updateCrt()
        if instruction.startswith('noop'):
            cycle += 1
        else:
            cycle += 1
            updateCrt()
            cycle += 1
            clearSprite(x)
            x += int(instruction[5:])
            drawSprite(x)

    print(term.move_yx(9, 0) + 'elf letter recognition program running ...', end='', flush=True)

    scannerWidth = 1
    letterPos = 0
    for i in range(40):
        greenScanLine(i)
        if scannerWidth >= 4:
            letter = letterRecognition(i+1-4, i+1)
            if letter != None:
                print(term.move_yx(7, letterPos) + letter, end='', flush=True)
                letterPos += 1
            clearScanLine(i-4)
        else:
            scannerWidth += 1
        sleep(0.3)

    clearScanLine(36)
    sleep(0.3)
    clearScanLine(37)
    sleep(0.3)
    clearScanLine(38)
    sleep(0.3)
    clearScanLine(39)
    sleep(0.3)

    print(term.move_yx(9, 0) + term.clear_eol + 'finished, press any key to quit ...', end='', flush=True)
    term.inkey()
