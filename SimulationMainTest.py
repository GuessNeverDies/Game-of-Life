# SimulationMain.py

import pygame as p
import Cell

WORLD_SIZE = 600
ROWS = COLS = 20
SQ_SIZE = WORLD_SIZE // ROWS

def main():
    screen = p.display.set_mode((WORLD_SIZE, WORLD_SIZE))
    clock = p.time.Clock()
    aliveCells = [(1, 4), (1, 3), (2, 2), (3, 5), (1, 2), (4, 2), (3, 1)]
    world = initializeWorld(aliveCells)
    done = False
    while not done:
        for event in p.event.get():
            if event.type == p.QUIT:
                done = True
        drawWorld(screen, world)
        updateWorld(world)
        newGeneration(world)
        calculateNeighbors(world)
        p.display.flip()
        clock.tick(.0002)

    p.quit()


def initializeWorld(aliveCellCoordinates):
    world = [] # create 2D list of all cell objects
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


def updateWorld(world):
    for row in world:
        for cell in row:
            cell.update()
            #print(world.index(row), row.index(cell), cell.isAlive, cell.aliveNextFrame)


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

            if (c == 0) and (r == 0):
                neighboringCoords.pop(5)
                neighboringCoords.pop(3)
                neighboringCoords.pop(2)
                neighboringCoords.pop(1)
                neighboringCoords.pop(0)
            elif (c == 19) and (r == 0):
                neighboringCoords.pop(7)
                neighboringCoords.pop(5)
                neighboringCoords.pop(3)
                neighboringCoords.pop(2)
                neighboringCoords.pop(1)
                neighboringCoords.pop(0)
            elif (c == 0) and (r == 19):
                neighboringCoords.pop(7)
                neighboringCoords.pop(6)
                neighboringCoords.pop(5)
                neighboringCoords.pop(3)
                neighboringCoords.pop(0)
            elif (c == 19) and (r == 19):
                neighboringCoords.pop(7)
                neighboringCoords.pop(6)
                neighboringCoords.pop(5)
                neighboringCoords.pop(4)
                neighboringCoords.pop(2)
            for i in range(len(neighboringCoords)):
                currentCell.moveableSquares.append(world[neighboringCoords[i][0]][neighboringCoords[i][1]])
                print(c, r, neighboringCoords[i], i)
                print(len(world), len(world[neighboringCoords[i][0]]))
if __name__ == "__main__":
    main()