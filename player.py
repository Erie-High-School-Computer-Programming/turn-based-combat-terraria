import random 

class Player:
    def __init__(self, name, damage, defense, health):
        """This method initializes the character
        It should give the character a name, attack, defense, and health stat
        It should also give the character a movelist"""
        self.name = name
        self.damage = damage
        self.defense = defense
        self.health = health
        self.attacks = {
                "move1" : {"damage": 14, "accuracy" :  80},
                "move2" : {"damage": 20, "accuracy" : 30},
                "move3" : {"damage": 60, "accuracy" : 13},
                "move4" : {"damage" : 5, "accuracy" : 100}
            }
   


        


        

    def attack(self, move, target):
        """This method should allow the character to attack another character using the 
        selected move. The move should deal damage to the target character"""
        attacks = self.damage

        if random.randint(1,100) < (self.moves_list["move1"]["accuracy"]):
            damage = 14
        else: 
            damage = 0

        if random.randint(1,100) < (self.moves_list["move2"]["accuracy"]):
            damage = 20
        else: 
            damage = 0
            
        if random.randint(1,100) < (self.moves_list["move3"]["accuracy"]):
            damage = 60
        else: 
            damage = 0
            
        if random.randint(1,100) < (self.moves_list["move3"]["accuracy"]):
            damage = 5
        else: 
            damage = 0

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    

        

    def __repr__(self):
        return f'{self.name}: Current HP: {self.health}'


    def display_stats(self):
        """This method should display the current health of the character"""
        pass

# p1 = Player("Re'Anna",100,90,1111,["move", "move2"])

# p1.attack("move", "cat")