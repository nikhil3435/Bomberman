from __future__ import print_function
from person import *
import copy


class Bomberman(Person):

    def __dropBomb(self, bomber, bomb, bord):
        '''Drop a bomb at the location of bomberman'''
        if bomb[0][0] is (-1):
            for i in range(len(bomber)):
                bord[bomber[i][0]][bomber[i][1]] = 3
                for j in range(len(bomber[i])):
                    bomb[i][j] = copy.deepcopy(bomber[i][j])
        else:
            return 0

    def func(self, typ, explosion, bomber, brick, x, y, bord, enemy, k):
        '''Do appropriate operation based on the type of object at explosion point'''
        if(typ == 'brick'):
            for i in range(2):
                for j in range(4):
                    brick.remove([x + i, y + j])
                    explosion.append([x + i, y + j])
                    bord[x + i][y + j] = 0
            k[0] += 20
        elif(typ == 'Wall'):
            return k
        elif (typ == 'bomber'):
            for i in range(2):
                for j in range(4):
                    explosion.append([x + i, y + j])
            for i in range(8):
                for j in range(2):
                    bomber[i][j] = (-1)
            # global lives
            k[1] -= 1
        elif (typ == 'empty'):
            for i in range(2):
                for j in range(4):
                    explosion.append([x + i, y + j])
        elif (typ == 'enemy'):
            for i in range(6):
                if [x, y] in enemy[i]:
                    enemy[i][0][0] = (-1)
            for i in range(2):
                for j in range(4):
                    bord[x + i][y + j] = 0
                    explosion.append([x + i, y + j])
            k[0] += 100
        return k

    def __bombExplode(
        self,
        bomber,
     bomb,
     brick,
     explosion,
     bord,
     lives,
     enemy,
     score):
        '''Make the bomb explode'''
        typel = self.type(bomb[0][0], bomb[0][1] - 4, bord, bomber)
        typer = self.type(bomb[0][0], bomb[0][1] + 4, bord, bomber)
        typeu = self.type(bomb[0][0] - 2, bomb[0][1], bord, bomber)
        typed = self.type(bomb[0][0] + 2, bomb[0][1], bord, bomber)
        k = []
        k.append(score)
        k.append(lives)
        print(k)
        options = [typel, typer, typeu, typed]
        x = [bomb[0][0], bomb[0][0], bomb[0][0] - 2, bomb[0][0] + 2]
        y = [bomb[0][1] - 4, bomb[0][1] + 4, bomb[0][1], bomb[0][1]]
        for i in range(4):
            k = self.func(
                options[i],
                explosion,
                bomber,
                brick, +
                x[i],
                y[i],
                bord,
                enemy,
                k)
        if [bomb[0][0], bomb[0][1]] in bomb and [bomb[0][0], bomb[0][1]] in bomber:
            k = self.func(
                'bomber',
                explosion,
                bomber,
                brick,
                bomb[0][0],
                bomb[0][1],
                bord,
                enemy,
                k)
        else:
            k = self.func(
                'empty',
                explosion,
                bomber,
                brick,
                bomb[0][0],
                bomb[0][1],
                bord,
                enemy,
                k)
        '''Removing the bomb from the current location'''
        for i in range(len(bomb)):
            bord[bomb[i][0]][bomb[i][1]] = 0
            for j in range(len(bomb[i])):
                bomb[i][j] = -1
        return k

    def __checkDeath(self, bomber, enemy, lives, ne):
        '''Check Whether the bomberman has died due to collision with an enemy'''
        for i in range(ne):
            if bomber[0][0] == enemy[i][0][0] and bomber[0][1] == enemy[i][0][1]:
                for i in range(8):
                    for j in range(2):
                        bomber[i][j] = (-1)
                lives -= 1
        return lives
