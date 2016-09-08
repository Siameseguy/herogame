import random

from character import Character
from battle import Battle
from monster import Imp
from monster import Goblin
from monster import Bandit

class Game:
  def setup(self):
    self.new = Character()
    self.monsters = [
      imp(),
      goblin(),
      bandit()
    ]

  def get_Monster(self):
    self.set_monster = random.choice(self.monsters)
    if self.set_monster != "":
      print("A {} approaches, ready for a fight.".format(self.set_monster))




Game()
   
