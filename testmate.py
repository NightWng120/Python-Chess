import player, board,pdb, copy, game

user = True
count = 0
checkmateTest = []
stalemateTest = [[[4, 1], [4, 2]], [[0, 6], [0, 4]], [[3, 0], [7, 4]], [[0, 7], [0, 5]], [[7, 4], [0, 4]], [[7, 6], [7, 4]], [[7, 1], [7, 3]], [[0, 5], [7, 5]], [[0, 4], [2, 6]], [[5, 6], [5, 5]], [[2, 6], [3, 6]], [[4, 7], [5, 6]], [[3, 6], [1, 6]], [[3, 7], [3, 2]], [[1, 6], [1, 7]], [[3, 2], [7, 6]], [[1, 7], [2, 7]], [[5, 6], [6, 5]], [[2, 7], [4, 5]]]

gameboard = board.Board()
white = player.Player(True)
black = player.Player(False)
colors = {True:white, False:black}

while count < 19:


    if user:
        white.movePiece(black, white.pieces[white.index(stalemateTest[count][0])], stalemateTest[count][1])
        black.filterPossibleMoves(white)
        user = not user
    else:
        black.movePiece(white, black.pieces[black.index(stalemateTest[count][0])], stalemateTest[count][1])
        white.filterPossibleMoves(black)
        user = not user

    count+=1

    black.filterPossibleMoves(white)
    white.filterPossibleMoves(black)
    piecesAll = white.pieces.copy()
    for i in black.pieces:
        piecesAll.append(i)
    gameboard.update(piecesAll)
    gameboard.printBoard()
    piecesAll.clear()

    if count == 19:
        pdb.set_trace()
    print(f"stalemate: {colors[user].stalemate(colors[not user].possibleMoves, black)}")
    print(f"hasWon: {game.hasWon(white, black, user)}")
    # print(f"{colors[user].kingP.check(colors[not user].possibleMoves)}")
    # print(f"{colors[user].kingP.moves(colors[not user].possibleMoves)}")
    print(f"Player: {user}")
        
