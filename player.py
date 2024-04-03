import king, queen, rook, knight, bishop, pawn, piece, math, numpy, pdb
class Player():
    possibleMoves = list()
    color = bool
    pieces = list()
    rooks = list()
    knights = list()
    bishops = list()
    pawns = list()
    queen = None
    king = None
    

    def __init__(self, color) -> None:
        self.color = color
        self.initPieces()


    def movePiece(self, player, piece, next):

            if piece.name.lower() == "p":
                print(piece.start)
                if self.take(player, next):
                    if piece.moveChoose(next, True) and self.collision(piece, player, next) and self.pieceLock(player, piece.position):
                    # if piece.moveChoose(next, True) and self.collision(piece, player, next):
                        for i,val in enumerate(player.pieces): #could technically return None if next doesn't correspond with a piece on the board somehow
                            if val.position == next:
                                player.pieces.pop(i)
                                piece.position = next
                                print("Take pawn move true")
                                return True
                    else:
                        print("Take pawn move not true")
                        return False

                elif piece.moveChoose(next, False) and self.collision(piece, player, next) and self.pieceLock(player, piece.position):
                # elif piece.moveChoose(next, False) and self.collision(piece, player, next):
                    piece.position = next
                    print("Pawn move true")
                    return True

                else:
                    print("Pawn move not true")
                    return False

            elif piece.moveChoose(next) and self.collision(piece, player, next) and self.pieceLock(player, piece.position):
            # elif piece.moveChoose(next) and self.collision(piece, player, next):
                if self.take(player, next):
                    for i,val in enumerate(player.pieces):
                        if val.position == next:
                            player.pieces.pop(i)
                            piece.position = next
                            print("Take move is true")
                            return True

                else:
                    piece.position = next
                    print("Move is true")
                    return True

            else:
                print("Move is not true")
                return False

    def initPieces(self):
        self.king = king.King(self.color)
        self.queen = queen.Queen(self.color)
        self.pieces = list()

        self.pieces.append(self.king)
        self.pieces.append(self.queen)

        self.rooks = list()
        for i in range(0, 2):
            self.rooks.append(rook.Rook(self.color))
            self.pieces.append(self.rooks[i])
        if self.color:
            self.rooks[0].setPos([0,0])
            self.rooks[1].setPos([7,0])

        else:
            self.rooks[0].setPos([0,7])
            self.rooks[1].setPos([7,7])

        self.knights = list()
        for i in range(0, 2):
            self.knights.append(knight.Knight(self.color))
            self.pieces.append(self.knights[i])

        if self.color:
            self.knights[0].setPos([1, 0])
            self.knights[1].setPos([6, 0])

        else:
            self.knights[0].setPos([1, 7])
            self.knights[1].setPos([6, 7])

        self.bishops = list()
        for i in range(0, 2):
            self.bishops.append(bishop.Bishop(self.color))
            self.pieces.append(self.bishops[i])

        if self.color:
            self.bishops[0].setPos([2, 0])
            self.bishops[1].setPos([5, 0])

        else:
            self.bishops[0].setPos([2, 7])
            self.bishops[1].setPos([5, 7])

        self.pawns = list()
        for i in range(0, 8):
            if self.color:
                self.pawns.append(pawn.Pawn(self.color))
                self.pawns[i].setPos([i,1])
            else:
                self.pawns.append(pawn.Pawn(self.color))
                self.pawns[i].setPos([i,6])

            self.pieces.append(self.pawns[i])

    def magnetude2d(self, vec): # POP POP
        return (math.sqrt(vec[0]**2 + vec[1]**2))

    def dotproduct2d(self, vec1, vec2):
        return vec1[0] * vec2[0] + vec1[1] * vec2[1]

    def isBetween(self, pos, next, inter):
        # determines if a piece is on an intersecting line between the current piece and a desired move location
        # Returns true if there is a piece between the current postion and the next position

        vectorInter = [inter[0] - pos[0], inter[1] - pos[1]]
        vectorNext = [next[0] - pos[0], next[1] - pos[1]]

        try:
            angle = numpy.degrees(numpy.arccos(self.dotproduct2d(vectorInter, vectorNext)/(self.magnetude2d(vectorInter) * self.magnetude2d(vectorNext))))

            posToNext = piece.Piece.dist(piece.Piece(), pos, next) # distance between current piece postion and desired move
            distancesSum = piece.Piece.dist(piece.Piece(), pos, inter) + piece.Piece.dist(piece.Piece(), inter, next) # the sum of the distances between the current piece postion and desired move postion with another piece

            if angle == 0 and posToNext == distancesSum:
                return True
            else:
                return False

        except ZeroDivisionError:
            print("Zero divison error")
            return False




        # return posToNext == distancesSum

    def collision(self, piece, player, next):
        # Returns true if the move is legal

        if piece.name.lower() == "n":
            for i in self.pieces:
                if i.position == next:
                    return False
            return True

        for i in self.pieces:
            if next == i.position and next != piece.position: # might be a redundant check
                pdb.set_trace()
                return False
            elif self.isBetween(piece.position, next, i.position):
                pdb.set_trace()
                return False
        for i in player.pieces:
            if(self.isBetween(piece.position, next, i.position) and next != i.position):
                pdb.set_trace()
                return False


        return True

    def pieceLock(self, player, pos):
        # return True
        # Returns False if a piece is locked in place

        for i in player.pieces:

            if i.name.lower() == ("q" or "r" or "b"):
                vectorPiece = [i.position[0] - pos[0], i.position[1] - pos[1]]
                vectorKing = [i.position[0] - self.king.position[0], i.position[1] - self.king.position[1]]
                angle = numpy.degrees(numpy.arccos(self.dotproduct2d(vectorPiece, vectorKing)/(self.magnetude2d(vectorPiece) * self.magnetude2d(vectorKing))))

                if angle != 0:
                    continue
                    # return True

                elif i.moveChoose(pos) and self.collision(i, self, pos):
                    pdb.set_trace()
                    return False

        return True

    def filterPossibleMoves(self, player):
        for i in self.pieces:
            buffer = i.redSpot()
            for j in buffer:
                if self.collision(player, i, j):
                    self.possibleMoves.append(j)

    def take(self, player, next):
        for i in player.pieces:
            if i.position == next:
                return True
        return False

    def index(self, pos):
        for i, val in enumerate(self.pieces):
            if val.position == pos: 
                return i

        return -1

    def printPieces(self):
        for i, val in enumerate(self.pieces):
            if i == len(self.pieces) - 1:
                print(f"{val.name}")
                break

            print(f"{val.name}, ", end="")
