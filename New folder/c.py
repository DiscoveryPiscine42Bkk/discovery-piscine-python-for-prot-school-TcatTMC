def rotate_board(board):
    """หมุนกระดานให้เป็นแนวตั้ง (Transpose)"""
    return [''.join(row) for row in zip(*board)]

def find_king(board):
    """ค้นหาตำแหน่งของ King บนกระดาน"""
    for y_idx, row in enumerate(board):
        for x_idx, cell in enumerate(row):
            if cell == 'K':
                return x_idx,y_idx
    return None

def find_pawns(board):
    """ค้นหาตำแหน่งของ Pawns (P) บนกระดาน"""
    pawns = []
    for row_idx, row in enumerate(board):
        for col_idx, cell in enumerate(row):
            if cell == 'P':
                pawns.append((row_idx, col_idx))
    return pawns


def is_attacked(board, kx, ky):
    """ตรวจสอบว่า King ถูกโจมตีหรือไม่"""
    n = len(board)

    # ทิศทางการเดินของหมากแต่ละประเภท
    directions = {
        'rook': [(0, 1), (0, -1), (1, 0), (-1, 0)],  # เดินแนวตรง
        'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # เดินแนวทแยง
        'queen': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],  # รวม Rook + Bishop
    }
    pawn_attacks = [(1, -1), (1, 1)]  

    # ตรวจสอบ Rook, Bishop, Queen
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
                    break  # หมากตัวอื่นขวาง

    # ตรวจสอบ Pawn
    for dx, dy in pawn_attacks:
        px, py = kx + dx, ky + dy
        print(py,px,board[py][px])
        if 0 <= px < n and 0 <= py < n and board[py][px] == 'P':
            return True

    return False

def checkmate(board_str):
    """ตรวจสอบว่า King อยู่ในสถานะ Check หรือไม่"""
    board = board_str.strip().split("\n")
    rotated_board = rotate_board(board)  # หมุนกระดานแนวตั้ง

    king_pos = find_king(rotated_board)
    if not king_pos:
        print("Error")  # ถ้าไม่มี King ให้แสดง Error
        return

    kx, ky = king_pos
    if is_attacked(rotated_board, kx, ky):
        print("Success")
        print(find_king(board))
        pawn_positions = find_pawns(rotated_board)
        print("Pawns found at:", pawn_positions)
    else:
        print("Fail")
        print("K",find_king(board))
        pawn_positions = find_pawns(rotated_board)
        print("Pawns found at:", pawn_positions)
