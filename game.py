import pygame
import pygame as pg
from pieces import *
from drawpieces import *
from identifypiece import *

from calculate_moves import *

initial_pieces = initialize_pieces()
x_loc, y_loc = None, None
clicked = 0
count_possible = 0
possible_moves = []

piece = None
color = None

#board variables
boardLength = 8
size = 60
count = 0

#colors
white, black, red = (255, 255, 255), (0, 0, 0), (255, 0, 0)
brown = (173, 57, 12)
light_brown = (232, 150, 118)

#creating the display and caption
gameDisplay = pygame.display.set_mode((800, 800))
pygame.display.set_caption("ChessBoard")

gameExit = True

while gameExit:

    clicked = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_loc, y_loc = pygame.mouse.get_pos()
            clicked = 1

    gameDisplay.fill(white)

    if clicked == 1:
        piece, color, x_place, y_place = identify_piece(x_loc, y_loc, initial_pieces)
        if piece is None or color is None:
            print("Not a piece")
        for square in initial_pieces:
            if x_place == square[2] and y_place == square[3]:
                index = count_possible
                break
            count_possible += 1

        possible_moves = completemovecalculation(initial_pieces[count_possible], initial_pieces)
        print(possible_moves)

    draw_board(gameDisplay, light_brown, brown)

    draw_pieces(gameDisplay, initial_pieces)

    pygame.display.update()

pygame.quit()

quit()





