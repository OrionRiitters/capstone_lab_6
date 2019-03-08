
# This program abstracts a new data structure from what would otherwise be a 2-digit integer.
# Each unit will be refered to as a 'rect' and for purposes other than mathematical
# operation will act as a tuple. Each tuple contains an x coordinate and a y coordinate
# (54: x=5, y=4). Use getRectX/getRectY to access coordinates, otherwise treat as an int.

from math import floor
from constant import BOARD_SIZE

class Board:

    filledRects = []
    boardGraphic = []

    def initializeBoardGraphic():
        xAxis = []

        for i in range(0, 7):
            yAxis = [' [ ] ' for i in range(0, 7)]
            xAxis.append(yAxis)

        return xAxis

    boardGraphic = initializeBoardGraphic()


# The two methods below take rects (two digit integers) and return the x and y values.
# "getRectInt()" is useless but I might have used it somewhere and don't have thetime
# to fix that.
    def getRectX(self, rect):
        rect = int(rect)
        x = (floor(rect/10) * 10)
        return x

    def getRectY(self, rect):
        rect = int(rect)
        y = rect - self.getRectX(rect)
        return y

    def getRectInt(self, rect):
        return int(rect)

# Takes a rect and a player, adds a rect to filledRects[], then adds a symbol
# corresponding to the player to boardGraphic[]
    def fillCoordinate(self, rect, player):
        if player.type == 'Human':
            filler = ' [X] '
        else:
            filler = ' [O] '

        self.boardGraphic[BOARD_SIZE-self.getRectY(self.getRectInt(rect))][int(self.getRectX(self.getRectInt(rect))/10)] = filler
        self.filledRects.append(rect)
        player.filledRects.append(rect)


# Constructs a list from a column number, then returns true if that list has a length
# of 7.
    def checkColumnFull(self, column):
        columnStack = []

        for x in [self.getRectX(rect) for rect in self.filledRects]:
            if x == int(column)*10:
                columnStack.append(None)

        if len(columnStack) == 7:
            return True
        else:
            return False


# Creates a list from a column just like the method above, then sorts that list.
# Returns the value of the rect in which a piece will "fall".
    def findColumnTopRect(self, column):
        rectStack = []
        column = column*10
    
        for rect in self.filledRects:
            if self.getRectX(rect) == column:
                rectStack.append(rect)
        rectStack.sort()

        if not rectStack:
            return column
        else:
            return int(rectStack[len(rectStack)-1]) + 1
