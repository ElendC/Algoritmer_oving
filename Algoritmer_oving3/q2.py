

def queenSolver(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    counter = 0
    queen_placer(board, 0, n, solutions)
    for solution in solutions:
        counter += 1
        print(counter)
        for row in solution:
            print(" ".join(row))
        print("\n")
    return solutions


def queen_placer(board, row, n, solutions):
    if row == n:       #basecase
        solutions.append([row[:] for row in board])  #
    else:
        for col in range(n):
            if valid_placement(board, row, col, n):
                board[row][col] = 'Q'
                queen_placer(board, row+1, n, solutions)
                board[row][col] = '.'
    
def valid_placement(board, row, col, n):
    for i in range(n):
        if board[i][col] == 'Q':  #Check if row contains Q
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
    for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
        
    return True
        
queenSolver(10)


