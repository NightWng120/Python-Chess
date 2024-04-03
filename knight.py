import piece

class Knight(piece.Piece):

    def __init__(self, color) -> None:
        self.color = color
        if color:
            self.name = "N"
        else:
            self.name = "n"
        super().__init__()

    def moveChoose(self, next):
        dist = self.dist(self.position, next)
        slope = self.slope(self.position, next)
        if self.bound(next):
            if slope == .5 or slope == -.5 or slope == 2 or slope == -2:
                if dist > 2.1 and dist < 2.3:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
