import pygame
from pieces import *

bp = pygame.image.load('Black_Pawn.png')
bkn = pygame.image.load('Black_Knight.png')
bb = pygame.image.load('Black_Bishop.png')
br = pygame.image.load('Black_Rook.png')
bq = pygame.image.load('Black_Queen.png')
bk = pygame.image.load('Black_King.png')

wp = pygame.image.load('White_Pawn.png')
wkn = pygame.image.load('White_Knight.png')
wb = pygame.image.load('White_Bishop.png')
wr = pygame.image.load('White_Rook.png')
wq = pygame.image.load('White_Queen.png')
wk = pygame.image.load('White_King.png')

#white pieces


def white_pawn(x, y, gameDisplay):
    gameDisplay.blit(wp, (x,y))

def white_rook(x, y, gameDisplay):
    gameDisplay.blit(wr, (x,y))

def white_knight(x, y, gameDisplay):
    gameDisplay.blit(wkn, (x,y))

def white_bishop(x, y, gameDisplay):
    gameDisplay.blit(wb, (x,y))

def white_queen(x, y, gameDisplay):
    gameDisplay.blit(wq, (x,y))

def white_king(x, y, gameDisplay):
    gameDisplay.blit(wk, (x,y))


#black pieces

def black_pawn(x, y, gameDisplay):
    gameDisplay.blit(bp, (x,y))

def black_rook(x, y, gameDisplay):
    gameDisplay.blit(br, (x,y))

def black_knight(x, y, gameDisplay):
    gameDisplay.blit(bkn, (x,y))

def black_bishop(x, y, gameDisplay):
    gameDisplay.blit(bb, (x,y))

def black_queen(x, y, gameDisplay):
    gameDisplay.blit(bq, (x,y))

def black_king(x, y, gameDisplay):
    gameDisplay.blit(bk, (x, y))

def draw_board(gameDisplay, light_brown, brown):
    boardLength = 8
    size = 60
    count = 0
    for i in range(1, boardLength+1):
        for j in range(1, boardLength+1):
            if count % 2 == 0:
                pygame.draw.rect(gameDisplay, light_brown, [size*j, size*i, size, size])
            else:
                pygame.draw.rect(gameDisplay, brown, [size*j, size*i, size, size])
            count += 1
        count -= 1

def draw_pieces(gameDisplay, initial_position):

    boardLength = 8
    size = 60
    for i in range(1, boardLength + 1):
        for j in range(1, boardLength + 1):
            for square in initial_position:
                letter = char_to_number(square[2])
                if square[0] == "pawn" and square[1] == "w":
                    white_pawn((9-letter) * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "rook" and square[1] == "w":
                    white_rook((9-letter) * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "knight" and square[1] == "w":
                    white_knight((9-letter) * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "bishop" and square[1] == "w":
                    white_bishop((9-letter) * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "queen" and square[1] == "w":
                    white_queen(letter * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "king" and square[1] == "w":
                    white_king(letter * size, (9-square[3]) * size, gameDisplay)

                if square[0] == "pawn" and square[1] == "b":
                    black_pawn((9-letter) * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "rook" and square[1] == "b":
                    black_rook((9-letter) * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "knight" and square[1] == "b":
                    black_knight((9-letter) * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "bishop" and square[1] == "b":
                    black_bishop((9-letter) * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "queen" and square[1] == "b":
                    black_queen(letter * size, (9-square[3]) * size, gameDisplay)
                elif square[0] == "king" and square[1] == "b":
                    black_king(letter * size, (9-square[3]) * size, gameDisplay)
