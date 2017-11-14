from __future__ import print_function


class Wall():

    def create_board(self, board):
        '''For fixing the dimensions of the board and generating the walls on the board'''
        for i in range(2):
            for j in range(92):
                board[i][j] = 1
        for i in range(2, 36):
            for j in range(92):
                if j <= 3 or j >= 88:
                    board[i][j] = 1
                elif (i % 4 == 0 or i % 4 == 1) and (j % 8 <= 3):
                    board[i][j] = 1

        for i in range(36, 38):
            for j in range(92):
                board[i][j] = 1
