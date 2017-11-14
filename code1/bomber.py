from __future__ import print_function
from walls import *
from board import *
from person import *
from bomberman import *
from getchunix import *
import copy
import signal
import sys
import time
import os
from alarmexception import *
from enemy import *
import copy
from time import time
from state import *

'''Initialise various arrays for further use'''
bord = [[0 for y in range(92)] for x in range(38)]
bomber = [[2, 4], [2, 5], [2, 6], [2, 7], [3, 4], [3, 5], [3, 6], [3, 7]]
bric = []
brick = []
enemy = []
for i in range(40):
    enemy.append([])
bomb = [[-1, -1], [-1, -1], [-1, -1], [-1, -1],
        [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
explosion = [[-1, -1], [-1, -1], [-1, -1],
             [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
lives = 3
level = 1

getch = GetchUnix()


def alarmHandler(signum, frame):
    raise AlarmException


def take_input(timeout=1):
    '''To take input directly from terminal or to terminate after 1 second in case no input is recieved'''
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n...")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
arr = [0, 0]

w = Wall()  # Wall class
b = Board()  # Board class
e = Enemy()  # Enemy class


def generatebricks(val):
    '''generate val number of bricks at random positions on the board'''
    for i in range(val):
        k = b.generateRandomNumber(bord, bomber)
        # print(k)
        for i in range(2):
            for j in range(4):
                brick.append([k[0] + i, k[1] + j])
                bric.append([k[0] + i, k[1] + j])
                bord[k[0] + i][k[1] + j] = 2


def generateEnemies(num):
    '''Generate 'num' number of enemies at random positions on the board'''
    for i in range(num):
        e._Enemy__addEnemy(bord, enemy, i, bomber)


nb = 20  # Initialise number of bricks
ne = 6  # Initialise number of enemies

generatebricks(nb)
generateEnemies(ne)
pers = Bomberman()
counter = -5
w.create_board(bord)  # Fix all the walls on the matrix
j = 1
score = 0  # Initialise score to 0
save = time()  # save the current time
save2 = time()  # save the current time

cnt = 0
statename = "menuState"


def menufunc(
    bord,
     bomber,
     counter,
     explosion,
     bomb,
     statename):
    '''Don't start the game unless the player asks to do so'''
    while True:
        State(
            bord,
            bomber,
            counter,
            explosion,
            bomb,
            statename)
        signal.signal(signal.SIGALRM, alarmHandler)

        try:
            text = getch()
            signal.alarm(0)
            print(text)
            if(text == "s"):
                statename = "playState"
                return statename
            elif (text == "q"):
                sys.exit(0)
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        # os.system("tput reset")

statename = menufunc(
    bord,
     bomber,
     counter,
     explosion,
     bomb,
     statename)

# statename = "playState"
while True:
    print("Lives = ", lives, end="")
    print(" Score = ", score, end="")
    print(" Level = ", level)
    State(
        bord,
        bomber,
     counter,
     explosion,
     bomb,
     statename)  # Printing the current state of board

    if cnt is ne:
        '''Level to be increased so num of bricks and num of enemies increased,bricks reset'''
        for p in brick:
            bord[p[0]][p[1]] = 0
        bomber[0][0] = (-1)
        brick = []
        nb += 10
        ne += 6
        generatebricks(nb)
        j = 1
        generateEnemies(ne)

    if(bomber[0][0] == (-1)):  # Reinitialise the bomber
        bomber = [[2, 4], [2, 5], [2, 6],
                  [2, 7], [3, 4], [3, 5], [3, 6], [3, 7]]
    ch = take_input()
    if len(explosion) > 0:  # Reinitialise explosion array
        explosion = [[-1, -1], [-1, -1], [-1, -1], [
            -1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]

    if(lives == 0):
        '''Quit if the lives are zero'''
        print("GAME OVER!! :(")
        sys.exit(0)
    '''Move the player according to input recieved'''
    if (ch == 'q'):
        sys.exit(0)
    elif(ch == 'w'):
        pers._Person__move_Up(bomber, bord)
    elif(ch == 'a'):
        pers._Person__move_Left(bomber, bord)
    elif(ch == 's'):
        pers._Person__move_Down(bomber, bord)
    elif(ch == 'd'):
        pers._Person__move_Right(bomber, bord)
    elif(ch == 'b'):
        if bomb[0][0] is (-1):
            counter = 3
        pers._Bomberman__dropBomb(bomber, bomb, bord)
    cnt = 0
    curr = time()
    if(curr - save >= 1):  # Move the enemy if at least 1s has passed since the last movement
        if(counter >= (-1)):
            counter -= 1
        for i in range(6):
            if(enemy[i][0][0] == (-1)):
                cnt += 1
                continue
            elif j == 1:
                j = 2
            else:
                e._Enemy__moveEnemy(bord, enemy, i, bomber)
        save = curr
    curr2 = time()
    if (curr2 - save2 >= 0.6):  # Move the enemy if at least 1s has passed since the last movement
        for i in range(6, ne):
            if(enemy[i][0][0] == (-1)):
                cnt += 1
                continue
            else:
                e._Enemy__moveEnemy(bord, enemy, i, bomber)
        save2 = curr2
    lives = pers._Bomberman__checkDeath(
        bomber,
        enemy,
     lives,
     ne)  # Update the lives if Bomberman died due to an enemy
    if cnt is ne:
        print("You Win Level " + str(level) + " !!!")  # Increent Level by one
        level += 1

    if(counter == (-1)):
        arr = pers._Bomberman__bombExplode(
            bomber,
            bomb,
            brick,
            explosion,
            bord,
            lives,
            enemy,
            score)  # Make the bomb explode
        score = copy.deepcopy(arr[0])
        lives = copy.deepcopy(arr[1])
        counter -= 1
    os.system('tput reset')  # Clear the screen for next printing
