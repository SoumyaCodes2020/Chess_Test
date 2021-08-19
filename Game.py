# import pygame, like yeah, quite simple
import pygame

# create the Game Class
# this class will be responsible for handling game events, like the player moving a piece, or checking if a move is legal


class Game:
    def __init__(self, win):
        self.win = win
        # the boardState variable is **really** important. It is, THE BOARD, like, what did you think it was?
        # anyways, this variable stores the location and type of all of the pieces
        self.boardState = [['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR'],
                           ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
                           ['WR', 'WN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']]

    # this function, pretty self-explainatory, will draw the board. aka: the brown and peach squares
    def drawBoard(self):
        # change the below 2 variables to mess around with the board dimensions
        xsize = 8
        ysize = 8
        # looping through the x and y, so that we can get coordinates
        for x in range(xsize):
            for y in range(ysize):
                # simple math to figure out where we should draw the square using the x and y variables
                rect = pygame.Rect(x * (800 / xsize), y *
                                   (800 / ysize), 800 / xsize, 800 / ysize)
                # to figure out the color of the square that we are drawing, we can use logic
                # You see, if the y coordinate(between 1 - 8) is even, every square with an even coordinate in that row will be white, and odd will be black. eg. y = 4, x = 7 would be black
                # Vice-Versa for odd rows, eg. y = 5, x = 7 would be white
                if y % 2 == 0:
                    if x % 2 == 0:
                        pygame.draw.rect(self.win, (240, 217, 181), rect)
                    else:
                        pygame.draw.rect(self.win, (181, 136, 98), rect)

                else:
                    if x % 2 == 0:
                        pygame.draw.rect(self.win, (181, 136, 98), rect)
                    else:
                        pygame.draw.rect(self.win, (240, 217, 181), rect)

    # turning a string in boardState to image object by brute force
    def computeStrToImg(self, piece):
        # kinda simple, but yeah
        if piece == 0:
            return None

        elif piece == 'WR':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_R.png'), (100, 100))

            return img

        elif piece == 'WN':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_N.png'), (100, 100))

            return img

        elif piece == 'WB':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_B.png'), (100, 100))

            return img

        elif piece == 'WK':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_K.png'), (100, 100))

            return img

        elif piece == 'WQ':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_Q.png'), (100, 100))

            return img

        elif piece == 'WP':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/W_P.png'), (100, 100))

            return img

        elif piece == 'BR':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_R.png'), (100, 100))

            return img

        elif piece == 'BN':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_N.png'), (100, 100))

            return img

        elif piece == 'BB':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_B.png'), (100, 100))

            return img

        elif piece == 'BQ':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_Q.png'), (100, 100))

            return img

        elif piece == 'BK':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/B_K.png'), (100, 100))

            return img

        elif piece == 'BP':
            img = pygame.transform.scale(
                pygame.image.load('Sprites/BP.png'), (100, 100))

            return img
