import piece

class Bishop(piece.Piece):

    def __init__(self, color) -> None:
        self.color = color
        if color:
            self.name = "B"
        else:
            self.name = "b"
        super().__init__()

    def moveChoose(self, next):
        slope = self.slope(self.position, next)
        if self.bound(next):
            if slope == 1 or slope == -1:
                return True
            else:
                return False
        else:
            return False

