#Zork 2.021

#This is my first attempt at remaking a simple version of the incredible game Zork of which I have fond memories of.
#   I never got very far in the game because I was young when it was a DOS game but my parents had played it and drawn out the whole map
#   I found out relatively recently that it got thrown out :O >:( WTF!?!?!? Anyway...
#   My main memories of Zork besides the DOS version is Zork3; "Want some rye? 'Course ya do!"
#   Now you know.

#Define character classes
class Player():
    def __init__(self):
        pass

class Troll():
    def __init__(self):
        pass

class Human():
    def __init__(self):
        pass

class Wizard():
    def __init__(self):
        pass

class Undead():
    def __init__(self):
        pass

class Orc():
    def __init__(self):
        pass

#Define game starting point
class Start():
    def __init__(self):
        pass

    def __str__(self):
        return """You stand in front of a large stone castle. A draw bridge leads up to the huge wooden gates.
        Behind you, to the South, there is vast openness, long wavy grass as far as you can see."""

atStart = Start()
inGame = True
inPlains = False



print("""Welcome to Zork 2.021!

    To navigate, type the direction you wish to go, [north, south, east, west, straight, left, right, back].
    To pick up objects type "pick up [name of item]".
    To attack type "attack orc with axe", for example.
    To open doors or chests etc. type "open [item]".
    Type "help" anytime for help menu.

    Hit Enter to continue. """)

userInput = input()

while inGame == True:
    if userInput != "north" or userInput != "south" or userInput != "east" or userInput != "west" or userInput != "straight" or userInput != "back" or userInput != "left" or userInput != "right" or userInput != "Enter":
        print('What?')
        userInput = input()

print(atStart)

userInput = input()

if userInput == "north":
    print ('You cross the drawbridge. The wooden gate now looms straight in front of you. To the left you see a fading path that looks like it leads around the castle.')
else:
    print ('You are in the open plains surrounding the castle. Grass is all around you, nothing else in site. You hear only the sound of the wind.')
    inPlains = True
    userInput = input()



if inPlains == True and userInput != "north":
    print ('You are in the open plains surrounding the castle. Grass is all around you, nothing else in site. You hear only the sound of the wind.')
elif inPlains == True and userInput == "north":
    print(atStart)

userInput = input()



















#
