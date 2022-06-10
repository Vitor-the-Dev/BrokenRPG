class PlayerCharacter:
    def __init__(self, name, lifepoints, stats):
        self.name = name
        self.lifepoints = lifepoints
        self.stats = stats
    
    def add_stats(self, whichstat, magnetude):
        self.stats[whichstat] += magnetude
        
        
    def takedamage(self, damage, who):
        if who is 0:
            self.lifepoints = self.lifepoints - damage
        else:
            self.stats[4][who-1] = self.stats[4][who-1] - damage
    
#    def startgame(self):
    
        
class Opponent:
    def __init__(self, name, hp, attackbonus): #[list of enemies]
        self.name = name
        self.hp = hp
        self.attack = attackbonus
        
    def damage(self, damage, who):
        self.hp[who] = self.hp[who] - damage

        

                     
