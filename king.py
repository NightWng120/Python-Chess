import piece,pdb

class King(piece.Piece):

    def __init__(self, color) -> None:
        self.color = color
        if color:
            self.name = "K"
            self.position = [4, 0]
        else:
            self.name = "k"
            self.position = [4, 7]
        super().__init__()

    def moveChoose(self, next, filteredPossibleMoves):
        # This method determines if the inputted move position is legal and makes sure
        # that the king isnt moving into a possible check. The filteredPossibleMoves variable represents
        # the opposing players "filtered" possible attack positions
        slope = self.slope(self.position, next)
        dist = self.dist(self.position, next)
        if not self.bound(next):
            return False

        if (abs(slope) == 1 and (dist > 1.3 and dist < 1.5)) or ((abs(slope) == 0 or abs(slope) == 100) and dist == 1):
            if next in filteredPossibleMoves:
                # print("Can't move onto a red spot")
                return False
                    # pdb.set_trace()
            else:
                return True

        else:
            # print("Invalid move")
            return False

    def moves(self, filteredPossibleMoves):
        moveList = list()
        for i in range(0,8):
            for j in range(0, 8):
                if self.moveChoose([i, j], filteredPossibleMoves):
                    moveList.append([i, j])
        return moveList 
    
    def check(self, filteredPossibleMoves):
        # Returns True if the king's position equals
        # a position in the list of the opposing players "filtered" possible attacks
        for i in filteredPossibleMoves:
            if self.position == i:
                return True
        return False

    def mate(self, filteredPossibleMoves): 
        # Returns True if king has no moves and is in check
        moves = self.moves(filteredPossibleMoves)
        if not moves and self.check(filteredPossibleMoves):
            return True

    def stalemate(self, filteredPossibleMoves):
        # Returns True if king has no moves and isn't in check
        moveList = self.moves(filteredPossibleMoves)
        if not self.check(filteredPossibleMoves) and not moveList:
            return True
        else:
            return False
