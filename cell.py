from line import Line,Point

class Cell:
    def __init__(self, p1, p2, window=None, left=True, right=True, top=True, bottom=True):
        self.hasLeftWall = left
        self.hasRightWall = right
        self.hasTopWall = top
        self.hasBottomWall = bottom
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y
        self.window = window
        self.visited = False
        self.center = Point((self.x1+self.x2)/2, (self.y1+self.y2)/2)

    def draw(self):
        if self.window is None:
            return
        line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
        if self.hasLeftWall:
            self.window.drawLine(line, 'red')
        else:
            self.window.drawLine(line, 'white')
        line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
        if self.hasRightWall: 
            self.window.drawLine(line, 'red')
        else:
            self.window.drawLine(line, 'white')
        line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
        if self.hasTopWall:
            self.window.drawLine(line, 'red')
        else:
            self.window.drawLine(line, 'white')
        line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
        if self.hasBottomWall:
            self.window.drawLine(line, 'red')
        else:
            self.window.drawLine(line, 'white')

    def draw_move(self, to_cell, undo=False):
        if not undo:
            line = Line(self.center, to_cell.center)
            self.window.drawLine(line, 'red')
        else:
            line = Line(self.center, to_cell.center)
            self.window.drawLine(line, 'grey')