import random



class Character:

  def __init__(self, **stats):
    self.player_stats = []

    #generate stats
    self.player_name = input("What is your heros name? ")
    self.hp = random.randint(15, 30)
    self.speed = random.randint(10,20)

    self.player_stats.append(self.player_name)
    self.player_stats.append(self.hp)
    self.player_stats.append(self.speed)
  

  def list_stats(self):
    print("Name: {} \n HP: {} \n".format(self.player_name, self.hp))


    