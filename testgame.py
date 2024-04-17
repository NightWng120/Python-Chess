import player, board,pdb, copy, game

# board = board.Board()
# player1 = player.Player(True)
# player2 = player.Player(False)
# 
# piecesAll = player1.pieces
# [piecesAll.append(i) for i in player2.pieces]
# board.update(piecesAll)
# board.printBoard()
# 
# # [6,0] -> [5, 2]
# userIn = "    G1    , F3               "
# userIn = userIn.split(",")
# for i, val in enumerate(userIn):
#     userIn[i] = val.strip()
# 
# print(userIn)
# 
# boolean = player1.movePiece(player2, player1.pieces[player1.index(board.inputToPos(userIn[0]))], board.inputToPos(userIn[1]))
# # boolean = player1.movePiece(player1.pieces[player1.index([6,0])], player2, [7, 2])
# print(boolean)
# 
# piecesAll = player1.pieces
# [piecesAll.append(i) for i in player2.pieces]
# board.update(piecesAll)
# board.printBoard()

user = True
gameboard = board.Board()
white = player.Player(True)
black = player.Player(False)
colors = {True:white, False:black}
with open('input.txt', 'r') as f:
    data = f.readlines()
data = data[0].split('\n')
data.pop()
data = data[0].split(',')
print(data)


for i in data:


    if user:
        white.movePiece(black, white.pieces[white.index(gameboard.inputToPos(game.trim(i)[0]))], gameboard.inputToPos(game.trim(i)[1]))
        black.filterPossibleMoves(white)
        user = not user
    else:
        black.movePiece(white, black.pieces[black.index(gameboard.inputToPos(game.trim(i)[0]))], gameboard.inputToPos(game.trim(i)[1]))
        white.filterPossibleMoves(black)
        user = not user


    black.filterPossibleMoves(white)
    white.filterPossibleMoves(black)
    piecesAll = white.pieces.copy()
    for i in black.pieces:
        piecesAll.append(i)
    gameboard.update(piecesAll)
    gameboard.printBoard()
    piecesAll.clear()

    # if count == 19:
    #     pdb.set_trace()
    # print(f"stalemate: {black.stalemate(white.possibleMoves, white)}")
    # print(f"hasWon: {game.hasWon(white, black, user)}")
    # print(f"{colors[user].kingP.check(colors[not user].possibleMoves)}")
    # print(f"{colors[user].kingP.moves(colors[not user].possibleMoves)}")
    # print(f"Player: {user}")
