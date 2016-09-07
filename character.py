import random

class Character:
  hero_array = []

  def get_name(self):
    self.hero_name = input("What is your heros name?")
    if self.hero_name != "":
      self.hero_array.append(self.hero_name)
      print("You are in the game!")

    else:
      self.get_name()

  def __init__(self, **kwargs):
    self.get_name()

  def hero_stats(self):
    print("Hero Name: {}".format(self.hero_array[0]))
    