import piece

class Rook(piece.Piece):

    def __init__(self, color) -> None:
        self.color = color
        if color:
            self.name = "R"
        else:
            self.name = "r"
        super().__init__()

    def moveChoose(self, next):
        slope = self.slope(self.position, next)
        if self.bound(next):
            if slope == 0 or slope == 100:
                return True
            else:
                return False
        else:
            return False
