import player, board,pdb

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


    while game:

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

                if userIn == "error":
                    player = False
                    continue

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
