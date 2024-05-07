import player, board,pdb, copy, game

user = True
gameboard = board.Board()
white = player.Player(True)
black = player.Player(False)
colors = {True:white, False:black}
players = {True:"white", False:"black"}
with open('test1.txt', 'r') as f:
    data = f.readlines()
data = data[0].split('\n')
data.pop()
data = data[0].split(',')
state = False
# print(data)


piecesAll = white.pieces.copy()
for i in black.pieces:
    piecesAll.append(i)
gameboard.update(piecesAll)
gameboard.printBoard()
piecesAll.clear()
for i in data:


    if user:
        print(f": {i}")
        state = white.movePiece(black, white.pieces[white.index(gameboard.inputToPos(game.trim(i)[0]))], gameboard.inputToPos(game.trim(i)[1]))
        if not state:
            print("Invalid Move")
            break;
        state = False
        black.filterPossibleMoves(white)
        user = not user
    else:
        print(f": {i}")
        state = black.movePiece(white, black.pieces[black.index(gameboard.inputToPos(game.trim(i)[0]))], gameboard.inputToPos(game.trim(i)[1]))
        if not state:
            print("Invalid Move")
            break;
        state = False
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

    print(f"stalemate: {black.stalemate(white.possibleMoves, white)}")
    # print(f"hasWon: {game.hasWon(white, black, user)}")
    # print(f"Player {players[user]} is in check: {colors[user].kingP.check(colors[not user].possibleMoves)}")
    # print(f"{colors[user].kingP.moves(colors[not user].possibleMoves)}")
    # print(f"Player: {user}")
