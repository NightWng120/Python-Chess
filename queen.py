import piece

class Queen(piece.Piece):

    def __init__(self, color) -> None:
        self.color = color
        if color:
            self.name = "Q"
            self.position = [3, 0]
        else:
            self.name = "q"
            self.position = [3, 7]
        super().__init__()

    def moveChoose(self, next):
        slope = self.slope(self.position, next)
        if self.bound(next):
            if (slope == 1 or slope == -1) or (slope == 0 or slope == 100):
                return True
            else:
                return False
        else:
            return False

