#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random  # Adding for a random move by the RandomPlayer object
import time  # For time delay, so it doesn't all print at once.

moves = ['rock', 'paper', 'scissors']


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.2)


"""The Player class is the parent class for all of the Players
in this game"""


class Player:  # Parent class for all players
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


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


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def tied_round(one, two):
    return ((one == 'rock' and two == 'rock') or
            (one == 'scissors' and two == 'scissors') or
            (one == 'paper' and two == 'paper'))


def play_again_question():
    response = input("Play again? (y/n)")
    if response == "y":
        if __name__ == '__main__':
            game = Game(HumanPlayer(), RandomPlayer())  # Who's playing
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
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
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
        print("Player 1:")
        print_pause(self.p1_score)
        print("Player 2:")
        print_pause(self.p2_score)
        print("\n")

        results1 = self.p1_score
        results2 = self.p2_score
        if results1 == 3:
            print("Hooray! Player 1 has won the most rounds!")
            print("Player 2 has been defeated.\n")
            play_again_question()
        if results2 == 3:
            print("Incredible! Player 2 has won the most rounds!")
            print("Player 1 has been defeated.\n")
            play_again_question()

    def play_game(self):
        print_pause("Welcome to Rock, Paper, Scissors!")
        print_pause("How to play: Choose either rock, paper, or scissors.")
        print_pause("Rock beats scissors.")
        print_pause("Paper covers rock.")
        print_pause("Scissors cuts paper.")
        print_pause("First player to reach 3 points wins.")
        print_pause("You are Human (Player 1), playing against "
                    "the Computer (Player 2).")
        print_pause("Game start!")
        for round in range(1, 20):
            print(f"• • • Round {round} --> GO!")
            self.play_round()


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())  # Who is playing the game
    game.play_game()
