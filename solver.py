import subprocess
def isSafe(board,j,i,k):
    a = 0
    b = 0
    c= 0
    ocol = (j//3)*3
    orow = (k//3)*3
    while(a<9):
        if board[k][a]==i:
            return 0
        a+=1
    while(b<9):
        if board[b][j]==i:
            return 0
        b+=1
    while(c<(3)):
        b = 0
        while(b<3):
            if(board[orow+c][ocol+b]==i):
                return 0
            b+=1
        c+=1
    return 1

def isValidBoard(board):
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0  # Temporarily remove the number
                if not isSafe(board, col, num, row):
                    return False
                board[row][col] = num  # Restore the number
    return True

def solver(board,row,column):
    if(isValidBoard(board)==False):
        return False
    nextr = row
    nextc = column+1
    if(nextc==9):
        nextr = row+1
        nextc = 0
    if(nextr==9):
        with open ("board.txt","w") as f:
             
            for i in board:
                for j in i:
                    f.write(f"{j} ")
        f.close()
        return True
    
    i = 1
    
    if (board[row][column]!=0) :
        return solver(board,nextr,nextc)
        
    while(i<10):
        if(isSafe(board,column,i,row)and(board[row][column]==0)):
                    board[row][column] = i
                    if(solver(board,nextr,nextc)):
                         return True
                    board[row][column] = 0
        i+=1
    
    return False
     

board = []
with open("board.txt", "r") as f:
    for line in f:
        row = list(map(int, line.strip().split()))
        board.append(row)
    f.close()

if(solver(board,0,0)==False):
    with open ("board.txt","w") as f:
        f.write("False")
    f.close()
subprocess.Popen(["Python","solved.py"])