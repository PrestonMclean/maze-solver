from tkinter import Tk, BOTH, Canvas
from maze import Maze
from line import Point

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("window")
        self.canvas = Canvas(self.root, width=width, height=height, background="white")
        self.canvas.pack()
        self.isWindowRuning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.canvas.update()
        self.canvas.update_idletasks()

    def drawLine(self, line, fill):
        line.draw(self.canvas, fill)
    
    def runing(self):
        self.isWindowRuning = True
        while self.isWindowRuning:
            self.redraw()
        
    def close(self):
        self.isWindowRuning = False

def main():
    window = Window(800, 600)
    maze = Maze(5,5,25, Point(10,10), window)
    maze.solve()
    window.runing()

main()