#overall control method
from pieces import *

def calculate_moves(piece, all_pieces):
    future_move = []
    piece[2] = char_to_number(piece[2])

    if piece[0] == "bishop":
        future_move = bishop_moves(piece, all_pieces)
    elif piece[0] == "rook":
        future_move = rook_moves(piece, all_pieces)
    elif piece[0] == "queen":
        future_move = queen_moves(piece, all_pieces)
    elif piece[0] == "king":
        future_move = king_moves(piece, all_pieces)
    elif piece[0] == "knight":
        future_move = knight_moves(piece, all_pieces)
    elif piece[0] == "pawn" and piece[1] == "w":
        future_move = white_pawn_moves(piece, all_pieces)
    else:
        future_move = black_pawn_moves(piece, all_pieces)

    for move in future_move:
        move[0] = number_to_char(move[0])

    return future_move

#bishop


def bishop_moves(location, all_pieces):

    future_moves = []
    next_moves = []

    for i in range(8):
        next_move = [location[2] + i + 1, location[3] + i + 1]
        if isLocationOccupied(all_pieces, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2] + i + 1, location[3] - i - 1]
        if isLocationOccupied(all_pieces, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2] - i - 1, location[3] + i + 1]
        if isLocationOccupied(all_pieces, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2] - i - 1, location[3] - i - 1]
        if isLocationOccupied(all_pieces, next_move):
            break
        future_moves.append(next_move)

    future_moves = removeOutOfBoundariesMove(future_moves)

    return future_moves

#rook


def rook_moves(location, all_moves):

    future_moves = []
    next_move = []

    for i in range(8):
        next_move = [location[2] + i + 1, location[3]]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2], location[3] + i + 1]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2] - i - 1, location[3]]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2], location[3] - i - 1]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    future_moves = removeOutOfBoundariesMove(future_moves)

    return future_moves

#queen


def queen_moves(location, all_moves):

    future_moves = []
    next_moves = []

    for i in range(8):
        next_move = [location[2] + i + 1, location[3] + i + 1]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2] + i + 1, location[3] - i - 1]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2] - i - 1, location[3] + i + 1]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2] - i - 1, location[3] - i - 1]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2] + i + 1, location[3]]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2], location[3] + i + 1]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2] - i - 1, location[3]]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    for i in range(8):
        next_move = [location[2], location[3] - i - 1]
        if isLocationOccupied(all_moves, next_move):
            break
        future_moves.append(next_move)

    future_moves = removeOutOfBoundariesMove(future_moves)

    return future_moves

#knight


def knight_moves(location, all_moves):
    future_moves = []

    intermediate_moves = []

    intermediate_moves = [[location[2] + 2, location[3] + 1], [location[2] + 2, location[3] - 1], [location[2] - 2, location[3] + 1], [location[2] - 2, location[3] - 1], [location[2] + 1, location[3] + 2], [location[2] - 1, location[3] + 2], [location[2] + 1, location[3] - 2], [location[2] - 1, location[3] - 2]]

    for move in intermediate_moves:
        if not isLocationOccupied(all_moves, move):
            future_moves.append(move)

    future_moves = removeOutOfBoundariesMove(future_moves)

    return future_moves


def king_moves(location, all_moves):
    future_moves = []
    intermediate_moves = []

    intermediate_moves = [[location[2] + 1, location[3] + 1], [location[2] + 1, location[3]], [location[2], location[3] + 1], [location[2] - 1, location[3] - 1], [location[2] - 1, location[3]], [location[2], location[3] - 1], [location[2] - 1, location[3] + 1], [location[2] + 1, location[3] - 1]]
    for move in intermediate_moves:
        if not isLocationOccupied(all_moves, move):
            future_moves.append(move)

    future_moves = removeOutOfBoundariesMove(future_moves)

    return future_moves

#white pawn


def white_pawn_moves(location, all_moves):
    future_moves = []
    intermediate_moves = []
    if location[3] == 2:
        intermediate_moves = [[location[2], location[3] + 1], [location[2], location[3] + 2]]
    else:
        intermediate_moves = [[location[2], location[3] + 1]]

    for move in intermediate_moves:
        if not isLocationOccupied(all_moves, move):
            future_moves.append(move)
    #, [location[2] + 1, location[3] + 1], [location[2] - 1, location[3] + 1]

    if isLocationOccupied(all_moves, [location[2] + 1, location[3] + 1]):
        future_moves.append([location[2] + 1, location[3] + 1])

    if isLocationOccupied(all_moves, [location[2] - 1, location[3] + 1]):
        future_moves.append([location[2] - 1, location[3] + 1])

    return future_moves

#black pawn


def black_pawn_moves(location, all_moves):
    future_moves = []
    intermediate_moves = []
    if location[3] == 7:
        intermediate_moves = [[location[2], location[3] - 1], [location[2], location[3] - 2]]
    else:
        intermediate_moves = [[location[2], location[3] - 1]]

    for move in intermediate_moves:
        if not isLocationOccupied(all_moves, move):
            future_moves.append(move)
    # [location[2] + 1, location[3] + 1], [location[2] - 1, location[3] + 1]

    if isLocationOccupied(all_moves, [location[2] + 1, location[3] - 1]):
        future_moves.append([location[2] + 1, location[3] - 1])

    if isLocationOccupied(all_moves, [location[2] - 1, location[3] - 1]):
        future_moves.append([location[2] - 1, location[3] - 1])

    return future_moves


def removeOutOfBoundariesMove(future_moves):

    revised_future_moves = [move for move in future_moves if 1 <= move[0] <= 8 and 1 <= move[1] <= 8]

    return revised_future_moves


def isLocationOccupied(all_moves, future_position):
    for move in all_moves:
        if move[2] == future_position[0] and move[3] == future_position[1]:
            return True
    return False
