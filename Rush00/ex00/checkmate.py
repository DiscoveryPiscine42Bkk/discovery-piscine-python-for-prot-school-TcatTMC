#//////////////////////////////////////////////////////////// หาตัวใดๆ //////////////////////////////////////////////////
def scan_king(board):
    # หา king
    for y_idx, row in enumerate(board):
        for x_idx, cell in enumerate(row):
            if cell == 'K':
                return x_idx, y_idx
    return None

def scan_Queens(board):
    # หา Queen
    for y_idx, row in enumerate(board):
        for x_idx, cell in enumerate(row):
            if cell == 'Q':
                return x_idx, y_idx
    return None

def scan_Rooks(board):
    # หา Rooks
    for y_idx, row in enumerate(board):
        for x_idx, cell in enumerate(row):
            if cell == 'R':
                return x_idx, y_idx
    return None

def scan_Bishop(board):
    # หา Bishop
    for y_idx, row in enumerate(board):
        for x_idx, cell in enumerate(row):
            if cell == 'B':
                return x_idx, y_idx
    return None

def scan_pawns(board):
    # หา pawns
    pawns = []
    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell == 'P':
                pawns.append((col_idx, row_idx))
    return pawns

#////////////////////////////////////////////////////// check /////////////////////////////////////////////////////////

def scan_check(board, kx, ky):
    # ตรวจ K อยู่ในระยะ check ไหม
    n = len(board)
    
    # ทิศการกินของหมากแต่ละตัว
    directions = {
        'rook': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        'queen': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    }

    # check!!!
    for piece, moves in directions.items():
        for dx, dy in moves:
            x, y = kx, ky
            while 0 <= x + dx < n and 0 <= y + dy < n:
                x += dx
                y += dy
                if board[y][x] in "RBQ":
                    if (piece == 'rook' and board[y][x] in 'RQ') or \
                        (piece == 'bishop' and board[y][x] in 'BQ') or \
                        (piece == 'queen' and board[y][x] == 'Q'):
                        return True
                if board[y][x] != '.':
                    break 

    # เบี้ย check
    pos_pawn = scan_pawns(board)
    for px, py in pos_pawn:
        if (px-1,py-1)==(kx, ky) or (px+1,py-1)==(kx,ky):
            # print("Success")
            return True
        
    return False


def check_K(board_str):
    #พิจารณาว่า K โดนเช็คไหม
    board = board_str.strip().split("\n")

    king_pos = scan_king(board)
    if not king_pos:
        print("Error")  
        return

    kx, ky = king_pos
    if scan_check(board, kx, ky):
        print("Success")
        # print("p",scan_pawns(board))
        # print("k",scan_king(board))
    else:
        print("Fail")
        # print("p",scan_pawns(board))
        # print("k",scan_king(board))
        

