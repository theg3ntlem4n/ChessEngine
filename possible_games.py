from pieces import *
from possible_moves import *
pieces = initialize_pieces()

future_moves = []
current_moves = []

for piece in pieces:
    if piece[0]:
        current_moves = calculate_moves(piece, pieces)
        print(piece[0] + ": ")
        print(current_moves)
        future_moves.append(current_moves)
