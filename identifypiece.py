import pygame
from pieces import *

def identify_piece(x, y, initial_pieces):

    if x < 60 or y < 60 or x > 540 or y > 540:
        return None, None

    x_square, y_square = pixels_to_squares([x,y])

    return_index = None

    count = 0

    for square in initial_pieces:
        if x_square == char_to_number(square[2]) and y_square == square[3]:
            return_index = count

        count += 1
    if count == 0:
        return None, None
    else:
        return initial_pieces[return_index][0], initial_pieces[return_index][1], initial_pieces[return_index][2], initial_pieces[return_index][3]


def pixels_to_squares(pixel_coordinates):
    square = [None, None]

    if 60 < pixel_coordinates[0] < 120:
        square[0] = 1
    elif 120 < pixel_coordinates[0] < 180:
        square[0] = 2
    elif 180 < pixel_coordinates[0] < 240:
        square[0] = 3
    elif 240 < pixel_coordinates[0] < 300:
        square[0] = 4
    elif 300 < pixel_coordinates[0] < 360:
        square[0] = 5
    elif 360 < pixel_coordinates[0] < 420:
        square[0] = 6
    elif 420 < pixel_coordinates[0] < 480:
        square[0] = 7
    elif 480 < pixel_coordinates[0] < 540:
        square[0] = 8

    if 60 < pixel_coordinates[1] < 120:
        square[1] = 8
    elif 120 < pixel_coordinates[1] < 180:
        square[1] = 7
    elif 180 < pixel_coordinates[1] < 240:
        square[1] = 6
    elif 240 < pixel_coordinates[1] < 300:
        square[1] = 5
    elif 300 < pixel_coordinates[1] < 360:
        square[1] = 4
    elif 360 < pixel_coordinates[1] < 420:
        square[1] = 3
    elif 420 < pixel_coordinates[1] < 480:
        square[1] = 2
    elif 480 < pixel_coordinates[1] < 540:
        square[1] = 1

    return square[0], square[1]