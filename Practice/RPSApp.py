from enum import *
import random

class Turn(Enum):
    player = 0
    com = 1
    evaluate = 2

class Choice(Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"

class RPS(object):
    
    def __init__(self, turnCount):
        self.turn_count = turnCount
        self.turn = Turn.player
        self.player_choice = None
        self.computer_choice = None

    def PlayerChoose(self):
        
        raw_player_choice = raw_input("KEYPRESS (R = ROCK || P = PAPER || S = SCISSORS -> ")
        self.player_choice = None

        if raw_player_choice is 'R' or raw_player_choice is 'r':
            self.player_choice = Choice.ROCK
            self.turn = Turn.com
            return True

        if raw_player_choice is 'P' or raw_player_choice is 'p':
            self.player_choice = Choice.PAPER
            self.turn = Turn.com
            return True

        if raw_player_choice is 's' or raw_player_choice is "S":
            self.player_choice = Choice.SCISSORS                
            self.turn = Turn.com
            return True
            
        else:
            self.turn = Turn.player
            return False

    def ComputerChoose(self):
        raw_computer_choice = random.randrange(0, 2)
        self.computer_choice = None

        if raw_computer_choice is 0:
            self.computer_choice = Choice.ROCK
            self.turn = Turn.evaluate
            return True

        if raw_computer_choice is 1:
            self.computer_choice = Choice.PAPER
            self.turn = Turn.evaluate
            return True

        if raw_computer_choice is 2:
            self.computer_choice = Choice.SCISSORS                
            self.turn = Turn.evaluate
            return True
            
        else:
            self.turn = Turn.evaluate
            return False

    def EvaluateChoices(self):
        winner = None

        if self.player_choice is Choice.ROCK and self.computer_choice is Choice.SCISSORS:
            winner = "PLAYER"

        if self.player_choice is Choice.PAPER and self.computer_choice is Choice.ROCK:
            winner = "PLAYER"

        if self.player_choice is Choice.SCISSORS and self.computer_choice is Choice.PAPER:
            winner = "PLAYER"

        if self.computer_choice is Choice.ROCK and self.player_choice is Choice.SCISSORS:
            winner = "COMPUTER"

        if self.computer_choice is Choice.PAPER and self.player_choice is Choice.ROCK:
            winner = "COMPUTER"

        if self.computer_choice is Choice.SCISSORS and self.player_choice is Choice.PAPER:
            winner = "COMPUTER"

        if self.computer_choice is Choice.ROCK and self.player_choice is Choice.ROCK:
            winner = "NOONE"

        if self.computer_choice is Choice.PAPER and self.player_choice is Choice.PAPER:
            winner = "NOONE"

        if self.computer_choice is Choice.SCISSORS and self.player_choice is Choice.SCISSORS:
            winner = "NOONE"
                        
        print str.format("PLAYER CHOSE {0} || COMPUTER CHOSE {1}\n", str(self.player_choice), str(self.computer_choice))
        print str.format("{0} WINS!\n", winner)
        self.turn = Turn.player            
        return 1
    
    def runGame(self):
        turnCount = 0
        while(turnCount < self.turn_count):
            if self.turn is Turn.player:
                self.PlayerChoose()

            if self.turn is Turn.com:
                self.ComputerChoose()

            if self.turn is Turn.evaluate:
                turnCount += self.EvaluateChoices()

turnCount = raw_input("HOW MANY TURNS? -> ")
game = RPS(turnCount)
game.runGame()