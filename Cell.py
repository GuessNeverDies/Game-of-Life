# Cell.py
class Cell():
    def __init__(self, isAlive):
        self.isAlive = isAlive
        self.neighbors = [] #list of adjacent cell
        self.aliveNextFrame = None
        self.age = 0

    def update(self):
        # iterate through neighbors list and count alive cells
        count = 0
        for cell in self.neighbors:
            if cell.isAlive:
                count += 1
        if (count < 2 or count > 3) and self.isAlive: #uses math to determine if a cell should be alive next frame
            self.aliveNextFrame = False
        elif 2 <= count <= 3 and self.isAlive:
            self.aliveNextFrame = True
        elif (not self.isAlive) and count == 3:
            self.aliveNextFrame = True


    def nextGeneration(self): #changes isAlive to aliveNextFrame
        self.isAlive = self.aliveNextFrame