from board import Board
from player import Player
from rule_manager import RuleManager
from ui import UI
from random import randint


# This is my first attempt at an Object Oriented Python program so a lot of this is
# probably done incorrectly. It works though!

class Main:

    board = Board()
    hmnPlayer = Player('Human')
    cmpPlayer = Player('Computer')
    ruleManager = RuleManager()
    ui = UI()

# Begin game
    def initializeGame(self):

        initInput = self.ui.promptBeginGame()

        if initInput == 1:
            self.ui.renderBoard(self.board.boardGraphic)
            self.beginHmnTurn(self.hmnPlayer)
            self.ui.renderBoard(self.board.boardGraphic)

        while True:
            self.beginCmpTurn(self.cmpPlayer)
            self.ui.computerMoveDialogue()
            self.ui.renderBoard(self.board.boardGraphic)
            self.beginHmnTurn(self.hmnPlayer)
            self.ui.renderBoard(self.board.boardGraphic)


# Second half could be abstracted out but I am out of time.
    def beginHmnTurn(self, player):
        currentRect = -1

        while True:
            column = int(self.ui.promptUserMove())

            if not self.board.checkColumnFull(column):
                currentRect = self.board.findColumnTopRect(column)
                self.board.fillCoordinate(currentRect, player)

                break
            else:
                self.ui.fullColumnPrompt()
        if self.ruleManager.locatePossibleConnects(self.board, player, currentRect):
            self.ui.renderBoard(self.board.boardGraphic)
            self.ui.promptEndGame(player)

# Almost identical to beginHmnTurn save for the fourth line of code
    def beginCmpTurn(self, player):
        currentRect = -1

        while True:
            column = randint(0,6)

            if not self.board.checkColumnFull(column):
                currentRect = self.board.findColumnTopRect(column)
                self.board.fillCoordinate(currentRect, player)

                break
            
    
        if self.ruleManager.locatePossibleConnects(self.board, player, currentRect):
            self.ui.renderBoard(self.board.boardGraphic)
            self.ui.promptEndGame(player)


main = Main()
main.initializeGame()
