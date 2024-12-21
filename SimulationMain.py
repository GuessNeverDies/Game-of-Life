#SimulationMain.py

import pygame as p, random as r
import Cell, Buttons

WORLD_SIZE = 600 #pixels per row and col in the world
ROWS = COLS = 20 #num of cells per row and per col
SQ_SIZE = WORLD_SIZE // ROWS #size of square is pixels per row div by cells per row

def main():
    p.init() #initialize pygame
    aliveCellNumber = r.randint(40, ROWS * COLS // 2) #random amount of cells living
    screen = p.display.set_mode((WORLD_SIZE, WORLD_SIZE + 100)) #makes window
    clock = p.time.Clock() #makes clock
    aliveCells = [] #empty list of cells
    for i in range(aliveCellNumber):
        aliveCells.append((r.randint(0, 20), r.randint(0, 20))) #appends random coords to list
    initializeButtons(screen) #see function
    world = initializeWorld(aliveCells) #see function
    calculateNeighbors(world) #see function
    done = False #used in while loop
    speed = 2 #tickspeed per second
    while not done:
        for event in p.event.get():
            if event.type == p.QUIT: #if red X clicked, then stop while loop
                done = True
            elif event.type == p.MOUSEBUTTONDOWN: #if mouse clicked, check if any button is clicked
                click = p.mouse.get_pos()
                if 0 <= click[0] <= 200 and 600 <= click[1] <= 700:
                    speed += 1 #speed up
                elif 200 < click[0] <= 400 and 600 <= click[1] <= 700:
                    if speed > 1:
                        speed -= 1 #speed down
                    else:
                        pass
                elif 400 < click[0] <= 600 <= click[1] <= 700:
                    world, aliveCells = reset() #see function
                    speed = 2 #resets speed
        drawWorld(screen, world) #see function
        updateWorld(world) #see function
        newGeneration(world) #see function
        p.display.flip()
        clock.tick(speed) #uses clock


    p.quit() #quits pygame after while loop is done




def reset(): #used to reset the world
    aliveCellNumber = r.randint(40, ROWS * COLS // 2)
    aliveCells = []
    for i in range(aliveCellNumber):
        aliveCells.append((r.randint(0, 20), r.randint(0, 20)))
    world = initializeWorld(aliveCells) #see function
    calculateNeighbors(world) #see function
    return world, aliveCells

def initializeButtons(screen): #initializes the buttons
    background = p.draw.rect(screen, 'black', (0, 600, 600, 700)) #creates background rect
    buttonNames = ['SPEEDUP', 'SLOWDOWN', 'RANDOM RESET'] #list of names
    colors = ['green', 'red', 'blue'] #list of colors
    buttons = [] #empty list
    font = p.font.SysFont('Times New Roman', 20) #uses font
    template = p.Rect(0, 0, 200, 50) #creates template rect
    for i in range(3):
        button = Buttons.Button(buttonNames[i], colors[i]) #uses button class
        buttons.append(button)
    for i in range(len(buttons)):
        buttonPos = template.clamp(background).move(i * 200, 25) #uses template to move the button
        p.draw.rect(screen, buttons[i].color, (0 + 200 * i, 600, 200, 700))
        line = font.render(buttons[i].name, True, 'black')
        screen.blit(line, buttonPos.move(30, 12)) #displays the line of text
    return buttons

def initializeWorld(aliveCellCoordinates): #initializes the world
    world = [] #empty list for the cell classes
    for row in range(ROWS):
        world.append([])
        for col in range(COLS):
            if (col, row) in aliveCellCoordinates: #if alive, then create class with alive attribute
                world[row].append(Cell.Cell(True))
            else:
                world[row].append(Cell.Cell(False)) #if dead, then create class with dead attribute
    return world


def drawWorld(screen, world): #draws the world
    for r in range(len(world)):
        for c in range(len(world)):
            if world[r][c].isAlive:
                p.draw.rect(screen, 'PaleGreen4', (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE)) #alive, then green
            else:
                p.draw.rect(screen, 'gray', (c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE)) #dead, then gray
            p.draw.rect(screen, 'black', (c * SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE), 1) #border


def updateWorld(world): #updates world
    for row in world:
        for cell in row:
            cell.update() #see file


def newGeneration(world): #displays next generation
    for row in world:
        for cell in row:
            cell.nextGeneration() #see file


def calculateNeighbors(world): #calculates the neighbors for a cell
    for r in range(ROWS):
        for c in range(COLS):
            currentCell = world[r][c]
            neighboringCoords = [(c - 1, r - 1), (c, r - 1), (c + 1, r - 1),
                                 (c - 1, r),                 (c + 1, r),
                                 (c - 1, r + 1), (c, r + 1), (c + 1, r + 1),]
            for coord in neighboringCoords:
                if coord[0] in range(COLS) and coord[1] in range(ROWS):
                    currentCell.moveableSquares.append(world[coord[1]][coord[0]]) #appends the neighbors to the cell's neighbor list


if __name__ == "__main__":
    main()