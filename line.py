class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2
    
    def draw(self, canvas, fill):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill, width=2)
        canvas.pack()