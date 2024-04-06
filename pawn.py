import piece, pdb

class Pawn(piece.Piece):
    start = bool

    def __init__(self, color) -> None:
        self.color = color
        self.start = True
        if color:
            self.name = "P"
        else:
            self.name = "p"
        super().__init__()

    # Things that need to be accounted for
    # - The pawn being able to move twice on it's first move
    # - The pawn only being able to move diagonally in two forward directions and only
    #   being able to do so when taking another piece

    # Things I need to test for
    # - What the pawns color is, so I can determine which direction it can go
    # - Whether or not it's taking a piece, so that I know if it's allowed to move diagonally
    # - Whether or not it's the pawns first move, so that I know if it's allow to move 2 spaces

    # Ways to making the pawn moveChoose method better
    # - Splitting the sections into their own functions
    def moveChoose(self, next, take):
        slope = self.slope(self.position, next)
        dist = self.dist(self.position, next)
        
        if not self.bound(next):
            return False

        if not take:
            if (self.color) and (abs(slope) == 1 and next[1] > self.position[1] or slope == 100 and next[1] > self.position[1]):
                if self.start and (dist == 1 or dist == 2):
                    self.start = False
                    return True
                elif not self.start and dist == 1:
                    return True
                else:
                    return False

            elif (not self.color) and (abs(slope) == 1 and next[1] < self.position[1] or slope == 100 and next[1] < self.position[1]):
                if self.start and (dist == 1 or dist == 2):
                    self.start = False
                    return True
                elif not self.start and dist == 1:
                    return True
                else:
                    return False

        elif take and self.color and (abs(slope) == 1) and (self.position[1] < next[1]) and (dist > 1.3) and (dist < 1.5):
            return True

        elif take and not self.color and (abs(slope) == 1) and (self.position[1] > next[1]) and (dist > 1.3) and (dist < 1.5):
            return True
        else:
            return False

    def moves(self):
        moveList = list()
        for i in range(0,8):
            for j in range(0, 8):
                if self.moveChoose([i, j], True): # set take to true to see all possible attacks
                    moveList.append([i, j])
        return moveList 
