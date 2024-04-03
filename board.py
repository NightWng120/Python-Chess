class Board():
    gameBoard = list() 

    def __init__(self) -> None:
        self.board()

    def convert(self, strings):
        words = "";
        string_list = list();
        for i in strings:
            for j in i:
                words+=j;
            string_list.append(words);
            words = "";
        return string_list;

    def inputToPos(self, posIn):
        # converts tradition chess coordinates to 8x8 coordinates
        print(f"PosIn: {posIn}")
        return [ord(posIn[0].lower()) - 97, int(posIn[1]) - 1]

    def posToBoard(self, pos):
        # converts 8x8 coordinates to coordinates corresponding to empty spaces in the board array
        return [15 - 2*pos[1], 2 + 4*pos[0]]

    def print_list(self, string_list):
        count = 9;
        print("\n")
        for i, val in enumerate(string_list):
            if (i+1)%2 == 0:
                print(f"{count-1} {val}");
                count-=1;
            else:
                print(f"  {val}");
            if i > 15:
                print("    A   B   C   D   E   F   G   H  ");
        print("\n")

    def board(self):
        val = True;
        string = list("|-------------------------------|");
        strings = list();
        strings.append(string);
        for j in range(0,8):
            string = list();
            for i in range(0, 17):
                if (i+1)%2 == 0 and val:
                    val = False;
                    string.extend(list("   "));
                elif (i+1)%2 == 0 and not val:
                    val = True;
                    string.extend(list(" * "));
                else:
                    string.extend(list("|"));
            val = not val;
            strings.append(string);
            if j > 6:
                strings.append(list("|-------------------------------|"));
                continue;	
            strings.append(list("|---|---|---|---|---|---|---|---|"));
        self.gameBoard = strings

    def update(self, pieces):
        self.board()
        for i in pieces:
            # print(f"Pos coords: {i.position}")
            position = self.posToBoard(i.position)
            # print(f"Board coords: {position}")
            self.gameBoard[position[0]][position[1]] = i.name

    # print_board(convert(board()))
    def printBoard(self):
        self.print_list(self.convert(self.gameBoard))
