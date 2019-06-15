#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 25 20:35:00 2019

@author: akim0417
"""

from pieces import *

"""required methods

    1. calculate moves
    2. is the location valid?
    3. is it checkmate?
    4. can capture
"""


def completemovecalculation(position, initial_pieces):
    position[2] = char_to_number(position[2])
    future_moves = calculate_moves(position)
    future_moves = removeOutOfBoundariesMove(future_moves)

    for position in initial_pieces:
        future_moves = removeLocationOccupied(future_moves, position)

    if position[0] == "pawn":
        future_moves = specialpawncapture(future_moves, position)

    return future_moves


'''pass the type of piece as the first (ie: 1 - 8 for white pawn, 9 - 16 for black pawn, 17 - 18 for white rook, 19-20 for black rook, 21 - 22 for white knight, 23 - 24 for black knight, 25 - 26 for white bishop, 27 - 28 for black bishop, 29 for white queen, 30 for black queen, 31 for white king, 32 for black king
remember that when you're calling the function, call it like calculate_moves(locationofpieces[the type of pieces that you are trying to move or calculate the piece of)
for example
calculate_moves(locationofpieces[17]) for the white rook

move from up counterclockwise'''


def calculate_moves(position):

    left = 7
    right = 7
    up = 7
    down = 7

    top_right = 7
    top_left = 7
    bottom_left = 7
    bottom_right = 7

    future_moves = []

    #return the pawn moves

    if position[0] == "pawn" and position[1] == "w":
        if position[3] == 2:
            future_moves = [[position[2], position[3] + 2], [position[2], position[3] + 1], [position[2] - 1, position[3] + 1], [position[2] + 1, position[3] + 1]]
        else:
            future_moves = [[position[2], position[3] + 1], [position[2] - 1, position[3] + 1], [position[2] + 1, position[3] + 1]]

    if position[0] == "pawn" and position[1] == "b":
        if position[3] == 7:
            future_moves = [[position[2], position[3] - 2], [position[2], position[3] - 1], [position[2] - 1, position[3] - 1], [position[2] + 1, position[3] - 1]]
        else:
            future_moves = [[position[2], position[3] - 1], [position[2] - 1, position[3] - 1], [position[2] + 1, position[3] - 1]]

    #return the rook moves

    elif position[0] == "rook":
        for a in range(up):
            future_moves.append([position[2], position[3] + a + 1])
        for a in range(right):
            future_moves.append([position[2]+a + 1, position[3]])
        for a in range(down):
            future_moves.append([position[2], position[3] - a - 1])
        for a in range(left):
            future_moves.append([position[2] - a - 1, position[3]])

    #return the knight moves

    elif position[0] == "knight":
        future_moves = [[position[2] + 1, position[3] + 2], [position[2] - 1, position[3] + 2], [position[2] + 1, position[3] - 2], [position[2] - 1, position[3] - 2]]

    #return the bishop moves

    elif position[0] == "bishop":

        for x in range(top_right):
            future_moves.append([position[2]+ x + 1, position[3] + x + 1])
        for x in range(bottom_right):
            future_moves.append([position[2] + x + 1, position[3] - x - 1])
        for x in range(bottom_left):
            future_moves.append([position[2] - x - 1, position[3] - x - 1])
        for x in range(top_left):
            future_moves.append([position[2] - x - 1, position[3] + x + 1])

    #return the queen moves

    elif position[0] == "queen":

        for a in range(up):
            future_moves.append([position[2], position[3] + a + 1])
        for a in range(right):
            future_moves.append([position[2]+a + 1, position[3]])
        for a in range(down):
            future_moves.append([position[2], position[3] - a - 1])
        for a in range(left):
            future_moves.append([position[2] - a - 1, position[3]])
        for x in range(top_right):
            future_moves.append([position[2] + x + 1, position[3] + x + 1])
        for x in range(bottom_right):
            future_moves.append([position[2] + x + 1, position[3] - x - 1])
        for x in range(bottom_left):
            future_moves.append([position[2] - x - 1, position[3] - x - 1])
        for x in range(top_left):
            future_moves.append([position[2] - x - 1, position[3] + x + 1])
    elif position[0] == "king":
        future_moves.append([position[2], position[3] + 1])
        future_moves.append([position[2] + 1, position[3]])
        future_moves.append([position[2], position[3] - 1])
        future_moves.append([position[2] - 1, position[3]])
        future_moves.append([position[2] + 1, position[3] + 1])
        future_moves.append([position[2] + 1, position[3] - 1])
        future_moves.append([position[2] - 1, position[3] - 1])
        future_moves.append([position[2] - 1, position[3] + 1])

    return future_moves

#check and remove if the location is occupied

def specialpawncapture(future_moves, position):
    return_move = [future_moves[0], future_moves[1]]
    for move in future_moves:
        if isLocationOccupied([move[0] - 1, move[1] + 1], position) is True or isLocationOccupied([move[0] + 1, move[1] + 1], position) is True:

            return_move.append(move)

    return return_move

def removeLocationOccupied(future_moves, position):

    '''send_moves = []

    dist_from_left = position[2] - 1
    dist_from_left = 8 - position[2]

    up_right = 0
    up_left = 0
    down_left = 0
    down_right = 0'''

    send_moves = []

    for move in future_moves:
        if isLocationOccupied(move, position) is False:
            send_moves.append(move)

        if isLocationOccupied(move, position) is True:
            break
    return send_moves



    return send_moves

def isLocationOccupied(move, position):
    if move[0] == position[2] and move[1] == position[3]:
        return True
    else:
        return False

#check if the moves are in boundaries

def removeOutOfBoundariesMove(future_moves):

    revised_future_moves = [move for move in future_moves if 1 <= move[0] <= 8 and 1 <= move[1] <= 8]

    return revised_future_moves




