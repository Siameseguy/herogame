import random

class Monster:
  def __init__(self, **stats):
    # self.monster_stats = []

    #generate stats
    self.hp = random.randint(15,30)
    self.attack = random.randint(1,5)
    self.mon_ex = random.randint(3,4)
    self.speed = random.randint(10,20)

    #append to monster_stat array
    # self.player_stats.append(self.hp)
    # self.player_stats.append(self.attack)

class Imp(Monster):
  def __init__(self, **stats):
    # self.monster_stats = []

    #generate stats
    self.hp = random.randint(5,8)
    self.attack = random.randint(1,5)
    self.mon_ex = random.randint(3,4)
    self.speed = random.randint(10,20)

    #append to monster_stat array
    # self.player_stats.append(self.hp)
    # self.player_stats.append(self.attack)

class Goblin(Monster):
  def __init__(self, **stats):
    # self.monster_stats = []

    #generate stats
    self.hp = random.randint(6,9)
    self.attack = random.randint(2,5)
    self.mon_ex = random.randint(4,5)
    self.speed = random.randint(10,20)

    #append to monster_stat array
    # self.player_stats.append(self.hp)
    # self.player_stats.append(self.attack)

class Bandit(Monster):
  def __init__(self, **stats):
    # self.monster_stats = []

    #generate stats
    self.hp = random.randint(7,10)
    self.attack = random.randint(3,6)
    self.mon_ex = random.randint(5,6)
    self.speed = random.randint(10,20)

    #append to monster_stat array
    # self.player_stats.append(self.hp)
    # self.player_stats.append(self.attack)