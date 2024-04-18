import player, board,pdb, copy

# - Go through all of the pieces of the player in check
# - Test each of its possible moves to see if it would stop their king from being in check
# - Make sure to reset each of the player variables after each time a movePiece call is made

def hasWon(white, black, player):
    # if playerW.movePiece(playerB, playerW.pieces[playerW.index(gameBoard.inputToPos(userIn[0]))], gameBoard.inputToPos(userIn[1])):
    w = copy.deepcopy(white)
    b = copy.deepcopy(black)
    w.filterPossibleMoves(b)
    b.filterPossibleMoves(w)

    if player:
        for i,val in enumerate(white.pieces):
            for j in w.pieces[i].possibleMoves:
                # print("We out here in white")
                if w.movePiece(b, w.pieces[i], j):
                    if w.kingP.check(b.possibleMoves):
                        w = copy.deepcopy(white)
                        b = copy.deepcopy(black)
                        continue
                    else:
                        return False
    elif not player:
        for i,val in enumerate(black.pieces):
            # print("We out here in black")
            for j in b.pieces[i].possibleMoves:
                if b.movePiece(w, b.pieces[i], j):
                    if b.kingP.check(w.possibleMoves):
                        b = copy.deepcopy(black)
                        w = copy.deepcopy(white)
                        continue
                    else:
                        return False
    return True





def trim(userIn):
    length = len(userIn)
    userIn = userIn.split(",")
    loop = True

    if len(userIn) < length and len(userIn) > 1:
        for i, val in enumerate(userIn):
            userIn[i] = val.strip()

    elif len(userIn) == 1:
        userIn = userIn[0].split(" ")
        
        while loop:
            try:
                userIn.remove('')
            except ValueError:
                loop = False
    return userIn

def playerPrompt(color, start, check):
    colors = {True:"White", False:"Black"}
    if start:
        if check:
            # pdb.set_trace()
            print( "|------------------------------|")
            print(f"|         Player {colors[color]}         |")
            print( "|------------------------------|")
            print( "|    Your king is in check     |")
            print( "|------------------------------|")
            print( "| Please enter the coordinates |")
            print( "| of your desired move         |")
            print( "|------------------------------|")
            print( "|     e.g. - A1, A2 | a1 a2    |")
            print( "|------------------------------|")
            print(": ", end="")
            userIn = input()
        else:
            print( "|------------------------------|")
            print(f"|         Player {colors[color]}         |")
            print( "|------------------------------|")
            print( "| Please enter the coordinates |")
            print( "| of your desired move         |")
            print( "|------------------------------|")
            print( "|     e.g. - A1, A2 | a1 a2    |")
            print( "|------------------------------|")
            print(": ", end="")
            userIn = input()

    else:
        if check:
            # pdb.set_trace()
            print( "|------------------------------|")
            print(f"|         Player {colors[color]}         |")
            print( "|------------------------------|")
            print( "|    Your king is in check     |")
            print( "|------------------------------|")
            print( "|     e.g. - A1, A2 | a1 a2    |")
            print( "|------------------------------|")
            print(": ", end="")
            userIn = input()
        else:
            print( "|------------------------------|")
            print(f"|         Player {colors[color]}         |")
            print( "|------------------------------|")
            print( "| Please enter the coordinates |")
            print( "| of your desired move         |")
            print( "|------------------------------|")
            print(": ", end="")
            userIn = input()

    return userIn


def chessGame(playerW, playerB):
    game = True
    start = True
    gameBoard = board.Board()
    piecesAll = list()
    player = True
    colors = {True: "White", False: "Black"}


    while game:
        # if playerW.kingP.stalemate(playerB.possibleMoves):
        #     piecesAll = playerW.pieces.copy()
        #     for i in playerB.pieces:
        #         piecesAll.append(i)
        #     gameBoard.update(piecesAll)
        #     gameBoard.printBoard()
        #     print()
        #     print(f"Stalemate! Player {colors[player]}'s king cannot move and isn't in check!")
        #     print()
        #     game = False
        #     continue

        # elif playerB.kingP.stalemate(playerW.possibleMoves):
        #     piecesAll = playerW.pieces.copy()
        #     for i in playerB.pieces:
        #         piecesAll.append(i)
        #     gameBoard.update(piecesAll)
        #     gameBoard.printBoard()
        #     print()
        #     print(f"Stalemate! Player {colors[player]}'s king cannot move and isn't in check!")
        #     print()
        #     game = False
        #     continue

        if hasWon(playerW, playerB, player):
            piecesAll = playerW.pieces.copy()
            for i in playerB.pieces:
                piecesAll.append(i)
            gameBoard.update(piecesAll)
            gameBoard.printBoard()
            print()
            print(f"Checkmate! Player {colors[not player]} has won the game!")
            print()
            game = False
            continue



        if player:
            try:
                player = False
                piecesAll = playerW.pieces.copy()
                for i in playerB.pieces:
                    piecesAll.append(i)
                gameBoard.update(piecesAll)
                gameBoard.printBoard()
                piecesAll.clear()
                # playerW.printPieces()

                # print("From playerB")
                # print(playerB.possibleMoves)
                # playerB.printPossibleMoves()

                playerB.filterPossibleMoves(playerW)
                userIn = playerPrompt(playerW.color, start, playerW.kingP.check(playerB.possibleMoves))

                if userIn.lower() == "quit":
                    print()
                    print("Quitting current game")
                    game = False
                    continue
                if userIn.lower() == "pdb":
                    pdb.set_trace()
                    player = True
                    continue

                userIn = trim(userIn)
                # print(f"inputToPos position: {gameBoard.inputToPos(userIn[0])}\ninputToPos next: {gameBoard.inputToPos(userIn[1])}")

                if playerW.movePiece(playerB, playerW.pieces[playerW.index(gameBoard.inputToPos(userIn[0]))], gameBoard.inputToPos(userIn[1])):
                    continue
                else:
                    print()
                    print("***Invalid move***")
                    print()
                    player = True
                    continue
            except (ValueError, IndexError, KeyboardInterrupt):
                print()
                print("***Invalid input***")
                print()
                player = True
                continue

        if not player:
            try:
                player = True
                piecesAll = playerW.pieces.copy()
                for i in playerB.pieces:
                    piecesAll.append(i)
                gameBoard.update(piecesAll)
                gameBoard.printBoard()
                piecesAll.clear()
                # playerB.printPieces()

                # print("From playerW")
                # print(playerW.possibleMoves)

                # playerW.printPossibleMoves()
                playerW.filterPossibleMoves(playerB)
                userIn = playerPrompt(playerB.color, start, playerB.kingP.check(playerW.possibleMoves))

                if userIn.lower() == "quit":
                    print()
                    print("Quitting current game")
                    game = False
                    continue

                if userIn.lower() == "pdb":
                    pdb.set_trace()
                    player = False
                    continue

                userIn = trim(userIn)


                # print(f"inputToPos position: {gameBoard.inputToPos(userIn[0])}\ninputToPos next: {gameBoard.inputToPos(userIn[1])}")

                if playerB.movePiece(playerW, playerB.pieces[playerB.index(gameBoard.inputToPos(userIn[0]))], gameBoard.inputToPos(userIn[1])):
                    start = False
                    continue
                else:
                    print()
                    print("***Invalid move***")
                    print()
                    player = False
                    continue
            except (ValueError, IndexError, KeyboardInterrupt):
                print()
                print("***Invalid input***")
                print()
                player = False
                continue
 

def main():
    main = True
    

    while(main):

        print()
        print("|--------------------------|")
        print("| Welcome to Python Chess! |")
        print("|--------------------------|")
        print("| 1) Start game            |")
        print("| 2) Help page             |")
        print("| 3) Quit game             |")
        print("|--------------------------|")
        print(": ", end="")

        userIn = input()

        if userIn == "1":
            playerW = player.Player(True)
            playerB = player.Player(False)
            chessGame(playerW, playerB)
                    

        elif userIn == "2":
            print()
            print()
            print("Help page coming soon!")
            print()
            print()

        elif userIn == "3":
            print()
            print("Quitting game...")
            print()
            main = False
            continue
        else:
            print("***Invalid input***")
            continue





if __name__ == '__main__':
    main()
