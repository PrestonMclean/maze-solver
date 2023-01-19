import unittest
from maze import Maze
from line import Point

class Tests(unittest.TestCase):
    def testCreateCells(self):
        numberRows = 10
        numbercolunm = 12
        maze = Maze(numberRows,numbercolunm,10, Point(10,10))
        self.assertEqual(
            len(maze.cells),
            numberRows
        )
        self.assertEqual(
            len(maze.cells[0]),
            numbercolunm
        )

    def testBreakEntranceAndExit(self):
        numberRows = 3
        numbercolunm = 3
        maze = Maze(numberRows,numbercolunm,10, Point(10,10))
        self.assertEqual(
            maze.cells[0][0].hasTopWall,
            False
        )
        self.assertEqual(
            maze.cells[numberRows-1][numbercolunm-1].hasBottomWall,
            False
        )

    def testResetVisited(self):
        numberRows = 3
        numbercolunm = 3
        maze = Maze(numberRows,numbercolunm,10, Point(10,10))
        for x in range(numberRows):
            for y in range(numbercolunm):
                self.assertEqual(
                    maze.cells[x][y].visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()