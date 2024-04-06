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


def chessGame(player1, player2):
    game = True
    start = True
    gameBoard = board.Board()
    piecesAll = list()
    player = True


    while game:

        if player:
            try:
                player = False
                piecesAll = player1.pieces.copy()
                for i in player2.pieces:
                    piecesAll.append(i)
                gameBoard.update(piecesAll)
                gameBoard.printBoard()
                piecesAll.clear()
                # player1.printPieces()

                # print("From player2")
                # print(player2.possibleMoves)
                player2.filterPossibleMoves(player1)
                userIn = playerPrompt(player1.color, start, player1.kingP.check(player2.possibleMoves))

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

                if player1.movePiece(player2, player1.pieces[player1.index(gameBoard.inputToPos(userIn[0]))], gameBoard.inputToPos(userIn[1])):
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
                piecesAll = player1.pieces.copy()
                for i in player2.pieces:
                    piecesAll.append(i)
                gameBoard.update(piecesAll)
                gameBoard.printBoard()
                piecesAll.clear()
                # player2.printPieces()

                # print("From player1")
                # print(player1.possibleMoves)

                player1.filterPossibleMoves(player2)
                userIn = playerPrompt(player2.color, start, player2.kingP.check(player1.possibleMoves))

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

                if player2.movePiece(player1, player2.pieces[player2.index(gameBoard.inputToPos(userIn[0]))], gameBoard.inputToPos(userIn[1])):
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
    colorChoose = True
    

    while(main):

        colorChoose = True
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
            while colorChoose:
                print()
                print("|-------------------|")
                print("| Choose your color |")
                print("|-------------------|")
                print("| 1) White          |")
                print("| 2) Black          |")
                print("|-------------------|")
                print(": ", end="")

                userIn = input()

                if userIn == "1":
                    player1 = player.Player(True)
                    player2 = player.Player(False)
                    chessGame(player1, player2)
                    colorChoose = False

                elif userIn == "2":
                    player1 = player.Player(False)
                    player2 = player.Player(True)
                    chessGame(player1, player2)
                    colorChoose = False
                else:
                    print()
                    print("***Invalid input***")
                    print()
                    continue
                    

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
