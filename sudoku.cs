// Sudoku solver
// Samuel Waggoner
// Began 1/10/22

public static class sudoku {

    public static void Main(string[] args) {
        Board board = new Board();
        board.PrintBoard()
        // for (int i = 1; i < )
        // Solve() 
    }

    public static array Solve(array board) {
        array origBoard = board;
        Console.WriteLine("Hi");

    }

    public static void PrintBoard(array board) {
        array printBoard = []

        if len(board) != 9:
            print("Incorrect board: number columns incorrect")
        for i in range(9):
            if len(board[i]) != 9:
                print("Incorrect board: Column " + str(i))

        # create numbers in right arrangement
        for i in range(9):
            row = []
            for j in range(9):
                row.append(board[j][i])
            row = str(row).replace('[','').replace(']','')
            printBoard.append(row)

        # add lines
        for i in range()
            print(row)
            /**
                0,0
                1,0
                2,0
                3,0
                ...
                0,1
                1,1
                2,1
                3,1
                4,1
                ...
            **/
    }
}

public class Board {
    
    public array boardArray;
    
    public Board() {
        return;
    }

    public void PrintBoard() {
        Console.WriteLine("Hello")
    }
}
