from classes.character import PlayerCharacter
from classes.generatemap import MapGraph
import random

mapsize = 100

name = input("You wake up in a strange, deeply unsettling jungle, somebody call your name")
PC = PlayerCharacter(name, 100, [1, 1, 1, [50, 50, 50]])
points = 10
print("Your squadmate helps you get up, which you do as fast as possible")

PC.add_stats(0, int(input("you have " + str(points) + " to distribute, how agile are you?")))

print("Looking around this forest, you begin to remember... you are in some form of combat training... you use your intellect to survey the situation")

PC.add_stats(1, int(input("you have " + str(points) + " to distribute, how smart are you?")))

print("You hear strange noises... unatural creatures as well as the enemy lurk around the corner... you prepare your weapon alongside your subordinates...")

PC.add_stats(2, int(input("you have " + str(points) + " to distribute, how combat-capable are you and your squad?")))


map = MapGraph().createmap(mapsize)


i = 0
#Loops through map nodes to find a "Nothing" node to begin
while i is 0:
    currentplace = map.find_node(random.randint(0, mapsize-1))
    if currentplace.value is not "nothing":
        print("no")
        continue 
    else:
        break

print(currentplace)

#add current place and move logic, add start battle logic and it's "done"

gameover = 0



