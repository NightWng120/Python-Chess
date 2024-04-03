import king, queen, rook, knight, bishop, pawn, board

kingW = king.King(True)
queenW = queen.Queen(True)
kingB = king.King(False)
queenB = queen.Queen(False)
pieces = list()

pieces.append(kingW)
pieces.append(queenW)
pieces.append(kingB)
pieces.append(queenB)

rooksW = list()
rooksB = list()
for i in range(0, 2):
    rooksW.append(rook.Rook(True))
    rooksB.append(rook.Rook(False))
    pieces.append(rooksW[i])
    pieces.append(rooksB[i])
rooksW[0].setPos([0,0])
rooksW[1].setPos([7,0])

rooksB[0].setPos([0,7])
rooksB[1].setPos([7,7])

knightsW = list()
knightsB = list()
for i in range(0, 2):
    knightsW.append(knight.Knight(True))
    knightsB.append(knight.Knight(False))
    pieces.append(knightsW[i])
    pieces.append(knightsB[i])

knightsW[0].setPos([1, 0])
knightsW[1].setPos([6, 0])

knightsB[0].setPos([1, 7])
knightsB[1].setPos([6, 7])

bishopsW = list()
bishopsB = list()
for i in range(0, 2):
    bishopsW.append(bishop.Bishop(True))
    bishopsB.append(bishop.Bishop(False))
    pieces.append(bishopsW[i])
    pieces.append(bishopsB[i])

bishopsW[0].setPos([2, 0])
bishopsW[1].setPos([5, 0])

bishopsB[0].setPos([2, 7])
bishopsB[1].setPos([5, 7])

pawnsW = list()
pawnsB = list()
for i in range(0, 8):
    pawnsW.append(pawn.Pawn(True))
    pawnsW[i].setPos([i,1])
    pawnsB.append(pawn.Pawn(False))
    pawnsB[i].setPos([i,6])
    pieces.append(pawnsW[i])
    pieces.append(pawnsB[i])

gameboard = board.Board()
gameboard.update(pieces)
gameboard.printBoard()
print(f"Piece at index 16: {pieces[16].getName()}")
# pieces[16].setPos([0,2])
pawnsW[0].setPos([0, 2])
print(f"Changed piece position at index 16: {pieces[16].getPos()}")
gameboard.update(pieces)
gameboard.printBoard()
