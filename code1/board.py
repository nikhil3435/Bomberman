from __future__ import print_function
from termcolor import colored
from random import *


class Board():

    def print_board(
        self,
        bord,
     bomber,
     counter,
     explosion,
     bomb,
    ):
        '''prints the game board'''
        for i in range(38):
            for j in range(92):
                if(bord[i][j] == 1):
                    print("X", end="")						# Walls
                elif([i, j] in bomber):
                    print(colored("B", "yellow"), end="")		# Bomberman
                elif bord[i][j] is 4 or bord[i][j] is -4:  # Normal Enemies
                    print(colored("E", "red"), end="")
                elif bord[i][j] is 5 or bord[i][j] is -5:  # Fast Enemies
                    print(colored("H", "red"), end="")
                elif(bord[i][j] == 2):
                    print(colored("/", "blue"), end="")		 # Brick
                elif([i, j] in bomb):
                    print(colored(counter, "magenta"), end="")  # Bomb
                elif([i, j] in explosion):
                    print(colored("e", "magenta"), end="")	 # Explosion
                else:
                    print(" ", end="")
            print("\n", end="")
        print("Press q to quit the game")

    def checkPiecePos(self, x, y, bord):
        '''check whether the piece position [x,y] is valid or not'''
        if(bord[x][y] is not 0):
            return bord[x][y]
        else:
            return 0

    def menu_state(self):
        '''print the menu state at the beginning of execution'''
        print("       MENU STATE")
        print("\n\n\n")
        print("press 's' to start the GAME")
        print("\n\n")
        print("press 'q' to quit the GAME")

    def movable(self, x, y, bord, bomber):
        '''Whether the given location is movable by the enemy'''
        if x > 1 and x < 36 and y > 3 and y < 88:
            if (bord[x][y] > 0):
                return 0
            else:
                return 1
        else:
            return 0

    def type(self, x, y, bord, bomber):
        '''Return the type of object present at [x,y]'''
        if bord[x][y] is 2:
            return 'brick'
        elif bord[x][y] is 1:
            return 'Wall'
        elif bord[x][y] is 4 or bord[x][y] is 5:
            return 'enemy'
        elif ((bord[x][y] is 0) and ([x, y] in bomber)):
            return 'bomber'
        elif (bord[x][y] is 0):
            return 'empty'

    def generateRandomNumber(self, bord, bomber):
        '''Generate Random Coordinates for placing brick or enemy'''
        x = 0
        y = 0
        while True:
            x = randint(1, 17)
            x *= 2
            if x % 4 == 0:
                y = randint(0, 9)
                y *= 8
                y += 4
            elif x % 4 != 0:
                y = randint(1, 20)
                y *= 4
            if bord[x][y] == 0 and ([x, y] not in bomber) and ([x, y] is not [2, 4]):
                return [x, y]
