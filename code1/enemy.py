from __future__ import print_function
from person import *
from board import *
from random import *


class Enemy(Person, Board):

    def __addEnemy(self, bord, enemy, enemyno, bomber):
        '''Add enemy on the board bsed on the random coordinates generated'''
        k = self.generateRandomNumber(bord, bomber)
        enemy[enemyno] = []
        for i in range(2):
            for j in range(4):
                enemy[enemyno].append([k[0] + i, k[1] + j])
                if i is 0:
                    if (enemyno <= 5):
                        bord[k[0] + i][k[1] + j] = 4
                    else:
                        bord[k[0] + i][k[1] + j] = 5
                elif i is 1:
                    if (enemyno <= 5):
                        bord[k[0] + i][k[1] + j] = -4
                    else:
                        bord[k[0] + i][k[1] + j] = -5
                # print(k[0]+i,k[1]+j)

    def __moveEnemy(self, bord, enemy, enemyno, bomber):
        '''Move the Enemy in one of the possible available directions'''
        r = 0
        if (enemy[enemyno][0][1]) is (-1):
            return
        x = enemy[enemyno][0][0]
        y = enemy[enemyno][0][1]
        flag = 0
        # print(self.movable(x,y,bord))
        if self.movable(x, y - 4, bord, bomber) == 0 and self.movable(x, y + 4, bord, bomber) == 0 and self.movable(x - 2, y, bord, bomber) == 0 and self.movable(x + 2, y, bord, bomber) == 0:
            return
        while True:
            r = randint(1, 4)
            '''Generte random number for choosing correct direction'''
            if r is 1:
                if self.movable(x, y - 4, bord, bomber) is 1:
                    self._Person__move_Left(enemy[enemyno], bord)
                    flag = 1
                    break
            elif r is 2:
                if self.movable(x, y + 4, bord, bomber) is 1:
                    self._Person__move_Right(enemy[enemyno], bord)
                    flag = 2
                    break
            elif r is 3:
                if self.movable(x - 2, y, bord, bomber) is 1:
                    self._Person__move_Up(enemy[enemyno], bord)
                    flag = 3
                    break
            elif r is 4:
                if self.movable(x + 2, y, bord, bomber) is 1:
                    self._Person__move_Down(enemy[enemyno], bord)
                    flag = 4
                    break

        for i in range(2):
            for j in range(4):
                k = bord[x + i][y + j]
                if(flag == 1):
                    bord[x + i][y + j - 4] = k
                elif(flag == 2):
                    bord[x + i][y + 4 + j] = k
                elif(flag == 3):
                    bord[x - 2 + i][y + j] = k
                elif(flag == 4):
                    bord[x + 2 + i][y + j] = k
                bord[x + i][y + j] = 0

        # print(enemyno,flag)
