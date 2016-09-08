import random



class Character:

  def __init__(self, **stats):
    self.player_stats = []

    #player hp


    #generate stats
    self.player_name = input("What is your heros name? ")
    self.hp = random.randint(15, 30)

    self.player_stats.append(self.player_name)
    self.player_stats.append(self.hp)
  

  def list_stats(self):
    print("Name: {} \n HP: {} \n".format(self.player_name, self.hp))
    