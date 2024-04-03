import player, board

board = board.Board()
player1 = player.Player(True)
player2 = player.Player(False)

piecesAll = player1.pieces
[piecesAll.append(i) for i in player2.pieces]
board.update(piecesAll)
board.printBoard()

# [6,0] -> [5, 2]
userIn = "    G1    , F3               "
userIn = userIn.split(",")
for i, val in enumerate(userIn):
    userIn[i] = val.strip()

print(userIn)

boolean = player1.movePiece(player2, player1.pieces[player1.index(board.inputToPos(userIn[0]))], board.inputToPos(userIn[1]))
# boolean = player1.movePiece(player1.pieces[player1.index([6,0])], player2, [7, 2])
print(boolean)

piecesAll = player1.pieces
[piecesAll.append(i) for i in player2.pieces]
board.update(piecesAll)
board.printBoard()
