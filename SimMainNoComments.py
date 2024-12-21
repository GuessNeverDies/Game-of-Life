import pygame as p, random as r
import Cell, Buttons

WORLD_SIZE = 600
ROWS = COLS = 20
SQ_SIZE = WORLD_SIZE // ROWS

def main():
    p.init()
    aliveCellNumber = r.randint(40, ROWS * COLS // 2)
    screen = p.display.set_mode((WORLD_SIZE, WORLD_SIZE + 100))
    clock = p.time.Clock()
    aliveCells = []
    for i in range(aliveCellNumber):
        aliveCells.append((r.randint(0, 20), r.randint(0, 20)))
    initializeButtons(screen)
    world = initializeWorld(aliveCells)
    calculateNeighbors(world)
    done = False
    speed = 2
    while not done:
        for event in p.event.get():
            if event.type == p.QUIT:
                done = True
            elif event.type == p.MOUSEBUTTONDOWN:
                click = p.mouse.get_pos()
                if 0 <= click[0] <= 200 and 600 <= click[1] <= 700:
                    speed += 1
                elif 200 < click[0] <= 400 and 600 <= click[1] <= 700:
                    if speed > 1:
                        speed -= 1
                    else:
                        pass
                elif 400 < click[0] <= 600 <= click[1] <= 700:
                    world, aliveCells = reset()
                    speed = 2
        drawWorld(screen, world)
        updateWorld(world)
        newGeneration(world)
        p.display.flip()
        clock.tick(speed)


    p.quit()




def reset():
    aliveCellNumber = r.randint(40, ROWS * COLS // 2)
    aliveCells = []
    for i in range(aliveCellNumber):
        aliveCells.append((r.randint(0, 20), r.randint(0, 20)))
    world = initializeWorld(aliveCells)
    calculateNeighbors(world)
    return world, aliveCells

def initializeButtons(screen):
    background = p.draw.rect(screen, 'black', (0, 600, 600, 700))
    buttonNames = ['SPEEDUP', 'SLOWDOWN', 'RANDOM RESET']
    colors = ['green', 'red', 'blue']
    buttons = []
    font = p.font.SysFont('Times New Roman', 20)
    template = p.Rect(0, 0, 200, 50)
    for i in range(3):
        button = Buttons.Button(buttonNames[i], colors[i])
        buttons.append(button)
    for i in range(len(buttons)):
        buttonPos = template.clamp(background).move(i * 200, 25)
        p.draw.rect(screen, buttons[i].color, (0 + 200 * i, 600, 200, 700))
        line = font.render(buttons[i].name, True, 'black')
        screen.blit(line, buttonPos.move(30, 12))
    return buttons

def initializeWorld(aliveCellCoordinates):
    world = []
    for row in range(ROWS):
        world.append([])
        for col in range(COLS):
            if (col, row) in aliveCellCoordinates:
                world[row].append(Cell.Cell(True))
            else:
                world[row].append(Cell.Cell(False))
    return world


def drawWorld(screen, world):
    for r in range(len(world)):
        for c in range(len(world)):
            if world[r][c].isAlive:
                p.draw.rect(screen, 'PaleGreen4', (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                p.draw.rect(screen, 'gray', (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            p.draw.rect(screen, 'black', (c * SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE), 1)


def updateWorld(world):
    for row in world:
        for cell in row:
            cell.update()


def newGeneration(world):
    for row in world:
        for cell in row:
            cell.nextGeneration()


def calculateNeighbors(world):
    for r in range(ROWS):
        for c in range(COLS):
            currentCell = world[r][c]
            neighboringCoords = [(c - 1, r - 1), (c, r - 1), (c + 1, r - 1),
                                 (c - 1, r),                 (c + 1, r),
                                 (c - 1, r + 1), (c, r + 1), (c + 1, r + 1),]
            for coord in neighboringCoords:
                if coord[0] in range(COLS) and coord[1] in range(ROWS):
                    currentCell.moveableSquares.append(world[coord[1]][coord[0]])


if __name__ == "__main__":
    main()