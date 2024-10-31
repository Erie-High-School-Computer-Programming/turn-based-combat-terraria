import random
# Create a game that allows players to choose between multiple characters
# and fight against each other. The game should have a simple combat system
# where characters can deal damage to each other. The game should also have
# a way to display the current health of each character.

# The game should have turned based combat where each player takes turns
# Players should have an attack, defense, and health stat

# Combat should involve a level of randomness.

# The game should have a way to display the current health of each character after each turn.

# Combat should continue until one of the characters health reaches 0.

# The game should have a way to display the winner of the game.

# The game should have a way to restart the game.

# The game should have a way to exit the game.
from player import Player


stacy = Player("Stacy", 25, 15, 120)
kim = Player("Kim", 25, 15, 120)
wallace = Player("Wallace", 25, 15, 120)
ramona = Player("Ramona", 25, 15, 120)

class Game:
    def __init__(self):
        """Initializes the game,
        It should give the game a list of at least 4 characters to choose from
        It should also give the game a list of moves for each character
        It should show player a list of characters to choose from
        and allow them to select a character,
        then have the computer choose a character at random
        It should randomly select a player to go first"""
        self.player_turn = random.choice([True, False])
        characters = [stacy, kim, wallace, ramona]
        moves = ["Acid", "Fire", "Punch", "Slam"]
        selecting = True

        while selecting:
            print(f"Choose your characters! \n{characters}")
            selection = input("What character would you like to choose? ").title()
            if selection == "Stacy" :
                print("You have chosen Stacy!")
                p1 = stacy
                selecting = False
            elif selection == "Kim":
                print("You have chosen Kim!")
                p1 = kim
                selecting = False
            elif selection == "Wallace" :
                print("You have chosen Wallace!")
                p1 = wallace
                selecting = False
            elif selection == "Ramona" :
                print("You have chosen Ramona!")
                p1 = ramona
                selecting = False
            else:
                print("That's not a character, Try again!")
    
            self.p1 = p1
            characters.remove(p1)
            self.player2 = random.choice(characters)
            player2 = self.player2
            print(f"Player 2 has chosen {player2}!")
        
        







    def turn(self):
        """This method should show the current health of both players, 
        and allow the player to select a move to use on the opponent
        If it is the computer player's turn, it should select a move at random"""
        
        if self.player_turn:
            print(self.p1.attacks)
            move = input("Choose your attack: ")
            pass
            if move == "quit":
                self.exit()
            elif move == "r" or move == "reset":
                self.playing = False
        self.player_turn = not self.player_turn
            
        p2_move = random.sample(self.attacks(), 1)

        if self.player2_turn:
            print(f"{self.player2} picked {self.player2.attacks}")

    def check_winner(self):
        """This method should check if either player's health has reached 0
        If a player's health has reached 0, it should display the winner"""
        pass

    def restart(self):
        """This method should allow the player to restart the game"""
        pass

    def exit(self):
        """This method should allow the player to exit the game"""

    def run(self):
        self.player_turn = True
        self.player2_turn = True
        self.playing = True
        while self.playing:
            self.turn()
            self.check_winner()

            


def main():
    playing = True
    while playing:
        game = Game()
        game.run()

main()