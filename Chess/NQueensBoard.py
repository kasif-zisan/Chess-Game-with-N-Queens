global N

N = 8
board = [
    ['bR', 'bN', 'bB', 'bR', 'bK', 'bB', 'bN', 'bR'],
    ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['--', '--', '--', '--', '--', '--', '--', '--'],
    ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
    ['wR', 'wN', 'wB', '--', 'wK', 'wB', 'wN', 'wR'],
]

whiteToMove = True


def attack(i, j):
    # checking vertically and horizontally
    for k in range(0, N):
        if board[i][k] == 'bQ' or board[i][k] == 'wQ' or board[k][j] == 'bQ' or board[k][j] == 'wQ':
            return True
    # checking diagonally
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 'bQ' or board[k][l] == 'wQ':
                    return True
    return False


def N_queens(n):
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not (attack(i, j))) and (board[i][j] != 'wQ' or board[i][j] != 'bQ'):
                save = board[i][j]
                if i <= 3:
                    board[i][j] = 'bQ'
                elif i > 3:
                    board[i][j] = 'wQ'
                if N_queens(n - 1):
                    return True
                board[i][j] = save
    return False


def move(startSq, endSq):
    startRow = startSq[0]
    startCol = startSq[1]
    endRow = endSq[0]
    endCol = endSq[1]
    pieceCaptured = board[endRow][endCol]
    pieceMoved = board[startRow][startCol]
    movedColor = board[startRow][startCol][0]
    capturedColor = board[endRow][endCol][0]
    if movedColor == capturedColor:
        print("You cannot attack your own")
    else:
        board[startRow][startCol] = '--'
        board[endRow][endCol] = pieceMoved
        if pieceCaptured == 'wK':
            print("BLACK HAS WON")
        elif pieceCaptured == 'bK':
            print("WHITE HAS WON")

def isValid(startSq, endSq):
    validFlag = True
    startRow = startSq[0]
    startCol = startSq[1]
    endRow = endSq[0]
    endCol = endSq[1]
    piece = board[startRow][startCol][1]
    pieceColor = board[startRow][startCol][0]
    if piece == 'P':
        if not movePawn(startRow, startCol, endRow, endCol, pieceColor):
            validFlag = False
    elif piece == 'R':
        if not moveRook(startRow, startCol, endRow, endCol):
            validFlag = False
    elif piece == 'N':
        if not moveKnight(startRow, startCol, endRow, endCol):
            validFlag = False
    elif piece == 'B':
        if not moveBishop(startRow, startCol, endRow, endCol):
            validFlag = False
    elif piece == 'Q':
        if not moveQueen(startRow, startCol, endRow, endCol):
            validFlag = False
    elif piece == 'K':
        if not moveKing(startRow, startCol, endRow, endCol):
            validFlag = False
    if validFlag:
        return True
    else:
        return False


def movePawn(startRow, startCol, endRow, endCol, pieceColor):
    if pieceColor == 'b' and startRow == 1 and ((startRow < endRow <= startRow + 2) or (
            startRow < endRow and (endCol == startCol + 1 or endCol == startCol - 1))):
        return True
    elif pieceColor == 'b' and startRow != 1 and ((startRow < endRow == startRow + 1) or (
            startRow < endRow and (endCol == startCol + 1 or endCol == startCol - 1))):
        return True
    elif pieceColor == 'w' and startRow == 6 and ((startRow > endRow >= startRow - 2) or (
            startRow > endRow and (endCol == startCol + 1 or endCol == startCol - 1))):
        return True
    elif pieceColor == 'w' and startRow != 6 and ((startRow > endRow == startRow - 1) or (
            startRow > endRow and (endCol == startCol + 1 or endCol == startCol - 1))):
        return True

    return False


def moveRook(startRow, startCol, endRow, endCol):
    if startCol != endCol and startRow != endRow:
        return False
    else:
        return True


def moveKnight(startRow, startCol, endRow, endCol):
    if (endCol == startCol + 1 or endCol == startCol - 1) and (endRow == startRow - 2 or endRow == startRow + 2):
        return True
    elif (endCol == startCol + 2 or endCol == startCol - 2) and (endRow == startRow - 1 or endRow == startRow + 1):
        return True
    else:
        return False


def moveBishop(startRow, startCol, endRow, endCol):
    if endCol > startCol and endRow > startRow:
        colMoved = endCol - startCol
        rowMoved = endRow - startRow
        if colMoved == rowMoved:
            return True
    elif endCol < startCol and endRow > startRow:
        colMoved = startCol - endCol
        rowMoved = endRow - startRow
        if colMoved == rowMoved:
            return True
    elif endCol < startCol and endRow < startRow:
        colMoved = startCol - endCol
        rowMoved = startRow - endRow
        if colMoved == rowMoved:
            return True
    elif endCol > startCol and endRow < startRow:
        colMoved = endCol - startCol
        rowMoved = startRow - endRow
        if colMoved == rowMoved:
            return True
    else:
        return False


def moveQueen(startRow, startCol, endRow, endCol):
    if moveBishop(startRow, startCol, endRow, endCol) or moveRook(startRow, startCol, endRow, endCol):
        return True
    else:
        return False

def moveKing(startRow, startCol, endRow, endCol):
    if endRow == startRow + 1 or endRow == startRow - 1 or endCol == startCol + 1 or endCol == startCol - 1:
        return True
    else:
        return False
