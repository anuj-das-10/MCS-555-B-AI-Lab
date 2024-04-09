def displayBoard(board: list) -> None:
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j] , end = "  ")
        print()
    print("\n")

#  Check all the direction  to see if there is a Queen.
def isSafe(board: list, row: int, col: int) -> bool:
    n = len(board)
    # 1. Check for 'Q' in particular row
    for j in range(n):
        if board[row][j] == 'Q': 
            return False

    # 2. Check for 'Q' in particular column
    for i in range(n):
        if board[i][col] == 'Q': 
            return False

    # 3. Check for 'Q' in North-West direction  
    r, c = row, col
    while(r >= 0 and c >= 0):
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1
    
    # 4. Check for 'Q' in South-East direction  
    r, c = row, col
    while(r < n and c < n):
        if board[r][c] == 'Q':
            return False
        r += 1
        c += 1

    # 5. Check for 'Q' in North-East direction  
    r, c = row, col
    while(r >= 0 and c < n):
        if board[r][c] == 'Q':
            return False
        r -= 1
        c += 1

    # 4. Check for 'Q' in South-West direction  
    r, c = row, col
    while(r >= n and c <= 0):
        if board[r][c] == 'Q':
            return False
        r += 1
        c -= 1        
    
    return True



def putQueen(board: list, row: int) -> None: 
    n = len(board)
    if row == n:
        global number_of_solutions
        number_of_solutions += 1
        displayBoard(board)
        return
    
    for j in range(n):
        if(isSafe(board, row, j)):
            board[row][j] = "Q"
            putQueen(board, row + 1)
            board[row][j] = "x"



def generateChessBoard(N: int) -> None:
    global board
    board = [["x" for _ in range(N)] for _ in range(N)]



# Driver Code
N = 4          #  N-Queen Problem
board = []
number_of_solutions = 0
generateChessBoard(N)
putQueen(board, 0)
print(f"Number of solutions for {N}-Queen in {N}X{N} Chess Board:  {number_of_solutions}")
