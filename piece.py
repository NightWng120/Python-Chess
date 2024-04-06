from abc import abstractmethod
import string
import math
class Piece():
    color = bool
    alive = bool
    position = list()
    possibleMoves = list()
    name = string



    def __init__(self) -> None:
        self.alive = True

    @abstractmethod
    def moveChoose(self, pos):
        pass


    def setPos(self, pos):
        self.position = pos

    def getPos(self):
        return self.position

    def getColor(self):
        return self.color

    def getName(self):
        return self.name
    
    def slope(self, pos, next):
        y = (next[1] - pos[1])
        x = (next[0] - pos[0])
        if y == 0 and x == 0:
            return 0
        elif x == 0:
            return 100
        else:
            return y/x

    def bound(self, pos):
        if pos[0] > 7 or pos[0] < 0 or pos[1] > 7 or pos[1] < 0:
            return False
        else:
            return True

    def dist(self, pos, next):
        if pos == next:
            return 0
        else:
            return math.sqrt((next[0] - pos[0])**2 + (next[1] - pos[1])**2)

    def moves(self):
        moveList = list()
        for i in range(0,8):
            for j in range(0, 8):
                if self.moveChoose([i, j]):
                    moveList.append([i, j])
        return moveList 
