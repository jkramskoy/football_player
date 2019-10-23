#prim itive data tipe

some_name = "Ninja"
age = 25
human = True
#last_name = None
size = 35.6

#data structures

canadian_cities_list = ["Winnipeg","Toronto","Edmonton"]  #list
emails_dict = {"someKey":human}    #dictinory

#functions
canadian_cities_list.sort()    #list-it is a data structure
canadian_cities_list.copy()

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
    def print(self):
        print(self.first_name + " " + self.last_name)

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    def height_to_feet(self):
        feet = self.height_cm * 0.0328084
        return feet


class BasketballPlayer(Player):
    def __init__(self,first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super ().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)

        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class Soccerplayer(Player):
    def __init__ (self, first_name, last_name, height_cm, weight_kg, gols, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.gols = gols
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

messi = Soccerplayer(first_name="Leonel",last_name="Messi",height_cm=109,weight_kg=98,gols=3,yellow_cards=4,red_cards=5)
messi.print()
print(messi.weight_to_lbs())

Lebronb = BasketballPlayer(first_name="Lebron",last_name="James",height_cm=203,weight_kg=113,points=27.2,rebounds=7.4,assists=7.2)
kev_dur = BasketballPlayer(first_name="Kevin",last_name="Durant",height_cm=210,weight_kg=108,points=27.2,rebounds=7.4,assists=7.2)
team = [Lebronb,kev_dur]

for player in team:
    player.print()

print(Lebronb.first_name + " " + Lebronb.last_name)
print(kev_dur.first_name + " " + kev_dur.last_name)

print(Lebronb.height_to_feet())
print(Lebronb.weight_to_lbs())

print(Lebronb.__dict__)




