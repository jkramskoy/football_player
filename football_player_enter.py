import json

class FootballPlayer():
    def __init__ (self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

#enter data
print("Enter some football player data")

first_name = input("please enter football player name: ")
last_name = input("Please enter football player last name: ")
height_cm = input("Please enter football player height: ")
weight_kg = input("Please enter football player weight: ")
goals = input("Please enter the number of player's goals: ")
yellow_cards = input("Please enter the number of player's yellow cards: ")
red_cards = input("Please enter the number of player's red cards: ")

#new player
new_player = FootballPlayer(first_name=first_name, last_name=last_name, height_cm=float(height_cm), weight_kg=float(weight_kg),
                            goals=int(goals), yellow_cards=int(yellow_cards), red_cards=int(red_cards))

#wright the file at text file
with open("football_player.txt","w")as football_file:
    football_file.write(json.dumps(new_player.__dict__))


print("Player successfully entered!")
print("Player's data: {0}".format(new_player.__dict__))



