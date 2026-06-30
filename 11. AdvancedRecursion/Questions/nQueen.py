#Q Leetcode-51 : 
def isSafe(row,col,board,n):
    duprow = row
    dupcol = col

    #check left upward diagonal
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    col = dupcol
    row = duprow
    #check in same row backside
    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1

    col = dupcol
    row = duprow
    #check left downward diagonal
    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False
        row += 1
        col -= 1
    return True
    
def NQueen(n):
    ans =[]
    board = ["." * n for _ in range(n)]
    def solve(col,board,ans,n):
        if col == n :
            ans.append(board.copy())
            return
        for row in range(n):
            if isSafe(row, col, board, n):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                solve(col+1, board, ans, n)
                board[row] = board[row][:col] + "." + board[row][col+1:]
    solve(0,board,ans,n)
    print(ans)

NQueen(4)

