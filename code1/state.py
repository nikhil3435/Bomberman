from board import *


class playState(Board):

    def draw(
        self,
        bord,
     bomber,
     counter,
     explosion,
     bomb,
    ):
        self.print_board(
            bord,
            bomber,
            counter,
            explosion,
            bomb,
        )


class menuState(Board):

    def draw(self):
        self.menu_state()


class State(Board):
    __play = playState()
    __menu = menuState()

    def __init__(
        self,
        bord,
     bomber,
     brick,
     explosion,
     bomb,
         statename):
        '''Function to depict polymophism and for printing the required contents on the screen'''
        if(statename == "playState"):
            self.__play.draw(
                bord,
                bomber,
                brick,
                explosion,
                bomb,
            )
        elif(statename == "menuState"):
            self.__menu.draw()
