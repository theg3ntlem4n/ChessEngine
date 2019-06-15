import pygame

def initialize_pieces():

    initial_pieces = []

    #first index is rows, second index is columns

    for x in range(0, 8):
        if x == 0:
            initial_pieces.append(["rook", "w", "A", 1])
            initial_pieces.append(["knight", "w", "B", 1])
            initial_pieces.append(["bishop", "w", "C", 1])
            initial_pieces.append(["queen", "w", "D", 1])
            initial_pieces.append(["king", "w", "E", 1])
            initial_pieces.append(["bishop", "w", "F", 1])
            initial_pieces.append(["knight", "w", "G", 1])
            initial_pieces.append(["rook", "w", "H", 1])
        elif x == 1:
            initial_pieces.append(["pawn", "w", "A", 2])
            initial_pieces.append(["pawn", "w", "B", 2])
            initial_pieces.append(["pawn", "w", "C", 2])
            initial_pieces.append(["pawn", "w", "D", 2])
            initial_pieces.append(["pawn", "w", "E", 2])
            initial_pieces.append(["pawn", "w", "F", 2])
            initial_pieces.append(["pawn", "w", "G", 2])
            initial_pieces.append(["pawn", "w", "H", 2])

        elif x == 6:
            initial_pieces.append(["pawn", "b", "A", 7])
            initial_pieces.append(["pawn", "b", "B", 7])
            initial_pieces.append(["pawn", "b", "C", 7])
            initial_pieces.append(["pawn", "b", "D", 7])
            initial_pieces.append(["pawn", "b", "E", 7])
            initial_pieces.append(["pawn", "b", "F", 7])
            initial_pieces.append(["pawn", "b", "G", 7])
            initial_pieces.append(["pawn", "b", "H", 7])
        elif x == 7:
            initial_pieces.append(["rook", "b", "A", 8])
            initial_pieces.append(["knight", "b", "B", 8])
            initial_pieces.append(["bishop", "b", "C", 8])
            initial_pieces.append(["queen", "b", "D", 8])
            initial_pieces.append(["king", "b", "E", 8])
            initial_pieces.append(["bishop", "b", "F", 8])
            initial_pieces.append(["knight", "b", "G", 8])
            initial_pieces.append(["rook", "b", "H", 8])
        else:
            for i in range(0, 8):
                initial_pieces.append([None, None, number_to_char(i+1), x+1])

    return initial_pieces


def number_to_char(num):
    if num == 1:
        return "A"
    elif num == 2:
        return "B"
    elif num == 3:
        return "C"
    elif num == 4:
        return "D"
    elif num == 5:
        return "E"
    elif num == 6:
        return "F"
    elif num == 7:
        return "G"
    elif num == 8:
        return "H"
    else:
        return


def char_to_number(cha):
    if cha == "A":
        return 1
    if cha == "B":
        return 2
    if cha == "C":
        return 3
    if cha == "D":
        return 4
    if cha == "E":
        return 5
    if cha == "F":
        return 6
    if cha == "G":
        return 7
    if cha == "H":
        return 8
    else:
        return

