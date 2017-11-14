from __future__ import print_function
from board import *


class Person(Board):

    def __move_Left(self, per, bord):
        '''Move the person left'''
        sum = 0
        for p in per:
            sum = sum + self.checkPiecePos(p[0], p[1] - 4, bord)
        if sum == 0:
            for p in per:
                p[1] -= 4
            return 1
        else:
            return 0

    def __move_Right(self, per, bord):
        '''Move the person right'''
        sum = 0
        for p in per:
            sum = sum + self.checkPiecePos(p[0], p[1] + 4, bord)
        if sum == 0:
            for p in per:
                p[1] += 4
            return 1
        else:
            return 0

    def __move_Up(self, per, bord):
        '''Move the person up'''
        sum = 0
        for p in per:
            sum = sum + self.checkPiecePos(p[0] - 2, p[1], bord)
        if sum == 0:
            for p in per:
                p[0] -= 2
            return 1
        else:
            return 0

    def __move_Down(self, per, bord):
        '''Move the person down'''
        sum = 0
        for p in per:
            sum = sum + self.checkPiecePos(p[0] + 2, p[1], bord)
        if sum == 0:
            for p in per:
                p[0] += 2
            return 1
        else:
            return 0
