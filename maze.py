import random
import time
from line import Point
from cell import Cell

class Maze:
    def __init__(self, numberOfRows, numberOfColumns, size, start=Point(10,10), window=None, seed=None):
        self.start = start
        self.rows = numberOfRows
        self.cols = numberOfColumns
        self.size = size
        self.window = window
        self.cells = []
        if seed:
            self.seed = random.seed(seed)
        self.createCells()
        self.breakEntranceAndExit()
        self.breakWalls(0,0)
        self.resetVisited()

    def createCells(self):
        for x in range(self.rows):
            row = []
            for y in range(self.cols):
                row.append(Cell(
                    Point(self.start.x + (x*self.size),self.start.y + (y*self.size)), 
                    Point(self.start.x + ((x+1)*self.size),self.start.y + ((y+1)*self.size)), self.window))
            self.cells.append(row)
        for x in range(self.rows):
            for y in range(self.cols):
                self.cells[x][y].draw()
                self.animate()

    def draw_cell(self, i, j):
        if self.window is None:
            return
        self.cells[i][j].draw()
        self.animate()

    def animate(self):
        if self.window is None:
            return
        self.window.redraw()
        time.sleep(.05)
    
    def breakEntranceAndExit(self):
        self.cells[0][0].hasTopWall = False
        self.cells[0][0].draw()
        self.cells[self.rows-1][self.cols-1].hasBottomWall = False
        self.cells[self.rows-1][self.cols-1].draw()

    def breakWalls(self,i,j):
        self.cells[i][j].visited = True
        while True:
            possibleCells = []
            numberOfCells = 0

            if i > 0 and not self.cells[i-1][j].visited:
                possibleCells.append((i-1,j))
                numberOfCells += 1
            
            if i < self.rows-1 and not self.cells[i+1][j].visited:
                possibleCells.append((i+1,j))
                numberOfCells += 1
            
            if j > 0 and not self.cells[i][j-1].visited:
                possibleCells.append((i,j-1))
                numberOfCells += 1

            if j < self.cols-1 and not self.cells[i][j+1].visited:
                possibleCells.append((i,j+1))
                numberOfCells += 1

            if numberOfCells == 0:
                self.draw_cell(i,j)
                return

            randomIndex = random.randrange(numberOfCells)
            nextCell = possibleCells[randomIndex]

            if nextCell[0] < i:
                self.cells[i][j].hasLeftWall = False
                self.cells[nextCell[0]][nextCell[1]].hasRightWall = False

            if nextCell[0] > i:
                self.cells[i][j].hasRightWall = False
                self.cells[nextCell[0]][nextCell[1]].hasLeftWall = False

            if nextCell[1] < j:
                self.cells[i][j].hasTopWall = False
                self.cells[nextCell[0]][nextCell[1]].hasBottomWall = False

            if nextCell[1] > j:
                self.cells[i][j].hasBottomWall = False
                self.cells[nextCell[0]][nextCell[1]].hasTopWall = False

            self.breakWalls(nextCell[0],nextCell[1])
    
    def resetVisited(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.cells[x][y].visited = False

    def solveR(self, i, j):
        self.animate()
        self.cells[i][j].visited = True

        if i == self.rows-1 and j == self.cols-1:
            return True

        if i > 0 and not self.cells[i][j].hasLeftWall and not self.cells[i-1][j].visited:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            if self.solveR(i-1,j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i-1][j],True)
        if i < self.rows-1 and not self.cells[i][j].hasRightWall and not self.cells[i+1][j].visited:
            self.cells[i][j].draw_move(self.cells[i+1][j])
            if self.solveR(i+1,j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i+1][j],True)
        if j < self.cols-1 and not self.cells[i][j].hasBottomWall and not self.cells[i][j+1].visited:
            self.cells[i][j].draw_move(self.cells[i][j+1])
            if self.solveR(i,j+1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j+1],True)
        if j > 0 and not self.cells[i][j].hasTopWall and not self.cells[i][j-1].visited:
            self.cells[i][j].draw_move(self.cells[i][j-1])
            if self.solveR(i,j-1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j-1],True)
        
        return False

    def solve(self):
        return self.solveR(0,0)