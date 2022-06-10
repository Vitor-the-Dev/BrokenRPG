import random

#https://codereview.stackexchange.com/questions/237601/simple-python-turn-based-battle-game


class Battle:
    def __init__(self):
        self.over = False
        self.round = 0
        
    def newRound(self):
        self.round += 1
        print("\n***   Round: %d   ***\n" %(self.round))
    
    def checkWin(self, player, opponent): #change
        if player.lifepoints < 1:
            self.gameOver = True
            print("You Lose")
            return -1
        elif len(opponent) == 0 and player.health > 0:
            self.gameOver = True
            print("You Win")
            return 1
        else:
            return 2
    
    def turn(self, player, opponent):
        moves = []
        enemymove = []

        #Collects input of the player, asking what he wishes to do (attack or defend) and how to order each squadmate
        for i in range(len(player.stats[4])):
            if i == 0:
                playeraction = input("Would you like to defend - D or attack - A")
                if playeraction is "A":
                    for j in range(len(opponent)):
                        print(opponent.name + " " + j)
                    input("Who should you attack? Select by inputting the number on your terminal")
                    
                elif playeraction == "D":
                    moves.append("D")
    
                else:
                    print("Invalid input!")
                    i= i-1
            else: 
                playeraction = input("What orders you give to your squadmate?")
                if playeraction is "A":
                    for j in range(len(opponent.name)):
                        print(opponent.name + " " + j)
                    moves.append(input("Who should your squadmate attack? Select by inputting the number on your terminal"))
                
                elif playeraction == "D":
                    moves.append("D")
                    continue   
                else:
                    print("Invalid input!")
                    i= i-1
                
        #opponent is a list carrying names and stats, will randomly attack player squad
        for i in range(len(opponent.name)):
            enemymove.append(random.randint(0, len(player.stats[4])-1))
        
        #Compute moves dealt into enemies based on STR stat    
        for i in moves:
            if i is 'A':
                opponent.damage(random.randint(1, player.stats[2]), i)
        
        for i in enemymove:
            if moves[i] is not 'D':
                
                player.takedamage(random.randinto(1, 10), i)
            else:
                player.takedamage(random.randinto(1, 10)*0.5, i)
                
        return Battle.checkWin(player, opponent)
        
        
    def main(self, player, opponent):
        end = 2
        while end is 2:
            Battle.newRound()
            end = Battle.turn(player, opponent)
        if end is 1:
            #return to the map, add a bonus stat for the player 
            return 1    
        else:
            #end campaing, you died
            return -2
        
        
        
            
