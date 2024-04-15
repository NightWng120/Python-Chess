import king, queen, rook, knight, bishop, pawn, piece, math, numpy, pdb, copy
class Player():
    possibleMoves = list()
    color = bool
    pieces = list()
    rooks = list()
    knights = list()
    bishops = list()
    pawns = list()
    queenP = queen.Queen(True)
    kingP = king.King(True)
    

    def __init__(self, color) -> None:
        self.possibleMoves = list()
        self.color = color
        self.initPieces()


    def movePiece(self, player, piece, next):
        # print(player.possibleMoves)
        # if piece.name == "b" and next == [6, 3]:
        #     pdb.set_trace()



        if piece.name.lower() == "p":
            # print(piece.start)
            # if self.color and piece.position == [5,2] and (next == [6,3] or next == [5,3]):
            #     pdb.set_trace()

            if self.take(player, next):
                if piece.moveChoose(next, True) and self.collision(piece, player, next):
                # if piece.moveChoose(next, True) and self.collision(piece, player, next):
                    for i,val in enumerate(player.pieces): #could technically return None if next doesn't correspond with a piece on the board somehow
                        if val.position == next:
                            playerPrev = player.pieces.pop(i)
                            prev = piece.position
                            piece.position = next
                            player.filterPossibleMoves(self)

                            if self.kingP.check(player.possibleMoves):
                                player.pieces.append(playerPrev)
                                piece.position = prev
                                self.filterPossibleMoves(player)
                                # print("Your king would be in check!")
                                return False

                            else:
                                self.filterPossibleMoves(player)
                                return True
                else:
                    self.filterPossibleMoves(player)
                    return False

            elif piece.moveChoose(next, False) and self.collision(piece, player, next):
            # elif piece.moveChoose(next, False) and self.collision(piece, player, next):
                prev = piece.position
                piece.position = next
                player.filterPossibleMoves(self)

                if self.kingP.check(player.possibleMoves):
                    piece.position = prev
                    self.filterPossibleMoves(player)
                    # print("Your king would be in check!")
                    return False

                else:
                    self.filterPossibleMoves(player)
                    return True

            else:
                self.filterPossibleMoves(player)
                return False

        elif piece.name.lower() == "k":
            # pdb.set_trace()
            if self.take(player, next):
                if piece.moveChoose(next, player.possibleMoves) and self.collision(piece, player, next):
                # if piece.moveChoose(next, True) and self.collision(piece, player, next):
                    for i,val in enumerate(player.pieces): #could technically return None if next doesn't correspond with a piece on the board somehow
                        if val.position == next:
                            playerPrev = player.pieces.pop(i)
                            prev = piece.position
                            piece.position = next
                            player.filterPossibleMoves(self)

                            if self.kingP.check(player.possibleMoves):
                                player.pieces.append(playerPrev)
                                piece.position = prev
                                # print("Your king would be in check!")
                                self.filterPossibleMoves(player)
                                return False

                            else:
                                self.filterPossibleMoves(player)
                                return True
                else:
                    self.filterPossibleMoves(player)
                    return False

            elif piece.moveChoose(next, player.possibleMoves) and self.collision(piece, player, next):
            # elif piece.moveChoose(next, False) and self.collision(piece, player, next):
                prev = piece.position
                piece.position = next
                player.filterPossibleMoves(self)

                if self.kingP.check(player.possibleMoves):
                    piece.position = prev
                    self.filterPossibleMoves(player)
                    # print("Your king would be in check!")
                    return False

                else:
                    self.filterPossibleMoves(player)
                    return True
            else:
                self.filterPossibleMoves(player)
                return False


        elif piece.moveChoose(next) and self.collision(piece, player, next):
        # elif piece.moveChoose(next) and self.collision(piece, player, next):
            if self.take(player, next):
                for i,val in enumerate(player.pieces):
                    if val.position == next:
                        playerPrev = player.pieces.pop(i)
                        prev = piece.position
                        piece.position = next
                        player.filterPossibleMoves(self)

                        if self.kingP.check(player.possibleMoves):
                            player.pieces.append(playerPrev)
                            piece.position = prev
                            # print("Your king would be in check!")
                            self.filterPossibleMoves(player)
                            return False

                        else:
                            self.filterPossibleMoves(player)
                            return True

            else:
                prev = piece.position
                piece.position = next
                player.filterPossibleMoves(self)

                if self.kingP.check(player.possibleMoves):
                    piece.position = prev
                    self.filterPossibleMoves(player)
                    # print("Your king would be in check!")
                    return False

                else:
                    self.filterPossibleMoves(player)
                    return True

        else:
            self.filterPossibleMoves(player)
            return False

    def initPieces(self):
        self.kingP = king.King(self.color)
        self.queenP = queen.Queen(self.color)
        self.pieces = list()

        self.pieces.append(self.kingP)
        self.pieces.append(self.queenP)

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
        # Returns true if there is a piece between the current position and the next position

        vectorInter = [inter[0] - pos[0], inter[1] - pos[1]]
        vectorNext = [next[0] - pos[0], next[1] - pos[1]]

        try:
            with numpy.errstate(invalid='ignore'):
                angle = numpy.degrees(numpy.arccos(self.dotproduct2d(vectorInter, vectorNext)/abs(self.magnetude2d(vectorInter) * self.magnetude2d(vectorNext))))

            posToNext = piece.Piece.dist(piece.Piece(), pos, next) # distance between current piece position and desired move
            distancesSum = piece.Piece.dist(piece.Piece(), pos, inter) + piece.Piece.dist(piece.Piece(), inter, next)# the sum of the distances between the current piece position and desired move position with another piece
            posToNext = math.trunc(posToNext*1000)/1000
            distancesSum = math.trunc(distancesSum*1000)/1000

            if (angle == 0 and posToNext == distancesSum) or (angle < 1 and angle > 0 and posToNext == distancesSum) or (angle > -1 and angle < 0 and posToNext == distancesSum):
                return True
            else:
                return False

        except ZeroDivisionError:
            # print("Zero divison error")
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
                # pdb.set_trace()
                return False
            elif self.isBetween(piece.position, next, i.position):
                # pdb.set_trace()
                return False
        for i in player.pieces:
            # if i.position == [5,2] and piece.position == [6,3]:
            #     pdb.set_trace()

            if(self.isBetween(piece.position, next, i.position) and next != i.position):
                return False


        return True

    def filterPossibleMoves(self, player):
        self.possibleMoves.clear()
        for i in self.pieces:
            if i.name.lower() == "k":
                buffer = i.moves(player.possibleMoves)
            else:
                buffer = i.moves()

            i.possibleMoves.clear()
            for j in buffer:
                if self.collision( i, player, j):
                    # if i.name.lower() == "q":
                    #     pdb.set_trace()
                    self.possibleMoves.append(j)
                    i.possibleMoves.append(j)
            for k in self.pieces:
                if k.position in self.possibleMoves:
                    self.possibleMoves.remove(k.position)
                if k.position in i.possibleMoves:
                    i.possibleMoves.remove(k.position)

            # print(f"{i.name}: {i.possibleMoves}")



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

    def printPossibleMoves(self):
        for i in self.pieces:
            print(f"{i.name}: {i.possibleMoves}")

    def stalemate(self, filteredPossibleMoves, player):
        # Returns True if king has no moves and isn't in check
        thisPlayer = copy.deepcopy(self)
        thatPlayer = copy.deepcopy(player)
        for i in thisPlayer.pieces:
            for j in i.possibleMoves:
                if thisPlayer.movePiece(thatPlayer, i, j):
                    return False
                thisPlayer = copy.deepcopy(self)
                thatPlayer = copy.deepcopy(player)
        # print(self.kingP.possibleMoves)
        if not self.kingP.check(filteredPossibleMoves) and not self.kingP.possibleMoves:
            return True
        else:
            return False
