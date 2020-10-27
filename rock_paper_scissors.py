#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random  # Adding for a random move by the RandomPlayer object
import time  # For time delay, so it doesn't all print at once.


class bcolors:
    RED = "\033[1;31m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    ENDC = '\033[0m'
    PURPLE = "\033[0;35m"


moves = ['rock', 'paper', 'scissors']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


"""The Player class is the parent class for all of the Players
in this game"""


class Player:  # Parent class for all players
    my_move = None  # Adding None so that the moves are None.
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move  # Got rid of 'pass' - adding code:
        self.their_move = their_move  # Defining my_move and their_move


class RandomPlayer(Player):  # Subclass of Player
    def move(self):
        return random.choice(moves)  # Picking a move at random


class HumanPlayer(Player):
    def move(self):
        human_move = input("Human, enter your move: rock, "
                           "paper, or scissors? > ").lower()
        while True:
            if human_move in moves:  # Keeps looping until move is accepted
                return human_move
            elif human_move != moves:
                human_move = input("Human, enter your move: rock, "
                                   "paper, or scissors? > ").lower()


class ReflectPlayer(Player):  # Remembers what opponent played last round
    def move(self):
        if self.their_move is None:
            return random.choice(moves)  # Gives a move instead of saying None
        else:
            while True:
                if self.their_move == 'rock':
                    return 'rock'
                elif self.their_move == 'scissors':
                    return 'scissors'
                elif self.their_move == 'paper':
                    return 'paper'


class CyclePlayer(Player):  # Remembers what move it played last round
    def move(self):         # and plays a different move the next round.
        if self.my_move is None:
            return random.choice(moves)  # Gives a move instead of saying None
        else:
            while True:
                if self.my_move == 'rock':
                    return 'paper'
                elif self.my_move == 'scissors':
                    return 'rock'
                elif self.my_move == 'paper':
                    return 'scissors'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def tied_round(one, two):
    return ((one == 'rock' and two == 'rock') or
            (one == 'scissors' and two == 'scissors') or
            (one == 'paper' and two == 'paper'))


def play_again_question():
    response = input("Play again? (y/n)").lower()
    if response == "y":
        if __name__ == '__main__':
            game = Game(CyclePlayer(), HumanPlayer())  # Who's playing
            game.play_game()
    if response == "n":
        quit()
    else:
        play_again_question()


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"{bcolors.CYAN}Player 1: {move1}{bcolors.ENDC} "
                    f"{bcolors.PURPLE}Player 2: {move2}{bcolors.ENDC}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):  # Determining who wins using beats fn
            self.p1_score += 1
            print_pause("* * * Player 1 wins this round * * *\n")
        elif beats(move1, move2):
            self.p2_score += 1
            print_pause("* * * Player 2 wins this round * * *\n")
        elif tied_round(move1, move2):
            print_pause("* * * It's a tie this round! * * *\n")
        else:
            self.p2_score += 1
            print_pause("* * * Player 2 wins this round * * *\n")
        print("The current score is:")  # This lets you know the current score
        print(f"{bcolors.CYAN}Player 1:")
        print_pause(self.p1_score)
        print(f"{bcolors.ENDC}{bcolors.PURPLE}Player 2:")
        print_pause(self.p2_score)
        print(f"\n{bcolors.ENDC}")

        results1 = self.p1_score
        results2 = self.p2_score
        if results1 == 3:
            print(f"{bcolors.RED}* * * GAME OVER * * * {bcolors.ENDC}")
            print(f"{bcolors.RED}Player 2 has been defeated.{bcolors.ENDC}")
            print(f"{bcolors.GREEN}Player 1 won the most "
                  f"rounds!{bcolors.ENDC}\n")
            print(f"Results:\n {bcolors.CYAN}Player 1 Final Score - "
                  f"{self.p1_score} point(s)\n {bcolors.ENDC}"
                  f"{bcolors.PURPLE}Player 2 Final Score - "
                  f"{self.p2_score} point(s).{bcolors.ENDC}")
            play_again_question()
        if results2 == 3:
            print(f"{bcolors.RED}* * * GAME OVER * * * {bcolors.ENDC}")
            print(f"{bcolors.RED}Player 1 has been defeated.{bcolors.ENDC}")
            print(f"{bcolors.GREEN}Player 2 won the most "
                  f"rounds!{bcolors.ENDC}\n")
            print(f"Results:\n {bcolors.CYAN}Player 1 Final Score - "
                  f"{self.p1_score} point(s)\n {bcolors.ENDC}"
                  f"{bcolors.PURPLE}Player 2 Final Score - "
                  f"{self.p2_score} point(s).{bcolors.ENDC}")
            play_again_question()

    def play_game(self):
        print_pause("Welcome to Rock, Paper, Scissors!")
        print_pause("How to play: Choose either rock, paper, or scissors.")
        print_pause("Rock beats scissors.")
        print_pause("Paper covers rock.")
        print_pause("Scissors cuts paper.")
        print_pause("First player to reach 3 points wins.")
        print_pause("A Computer Player named Cycle (Player 1) is "
                    "going to remember what it played last round and "
                    "play a different move the next round,"
                    "against a Human Player (Player 2).")
        print_pause("Game start!")
        for round in range(1, 20):
            print(f"• • • Round {round} --> GO!")
            self.play_round()


if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())  # Who is playing the game
    game.play_game()


#  How to use None ("is" vs "==") - https://www.educative.io/edpresso/
#                    what-is-the-none-keyword-in-python
#  Colors - https://godoc.org/github.com/whitedevops/colors
#  Colors - https://stackoverflow.com/questions/287871/how-
#            to-print-colored-text-in-python
#  Colors - https://gist.github.com/vratiu/9780109
