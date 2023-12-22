#the first issue and main issue was using print statements after every elif instead of just moving to the next variable input and having the story text be a part of the input text.
#Another big issue issue with this one was the indentation needed to be correct and have the else statements be in alignment below each corresponding if/else statement.
#For some reason though it seemed to not consistently indent when creating subsiquent if's or elif statements.

print("Welcome to Hogwarts.")
print("Your mission is to find the Triwizard Cup.")
print("You stand in the middle of the Great Hall looking at the owl pedestal where Dumbledore gives his yearly speaches.  There is a door infront of you and behind you.")
confused= "\nYou become confused and start quacking and flapping your arms like a duck for the rest of the night.\nGAME OVER"
# second = input("Which way do you choose? Stairs or Door: ").lower()
# third = input("Which do you choose? Up or Right: ").lower()
# fourth = input("Which door do you choose, the door on the right or the door on the left? R or L: ").lower()
# final = input("Which do you choose? Wardrobe, Chest, Curtain, or Somewhere else: ").lower
first_front="\nYou know students aren't allowed to go through that door! You get Dentention!\nGAME OVER"
first_back="\nYou find yourself in the Main Entrance to Hogwarts Castle. To your left there is a Staircase and in front of you is the Main Door that leads out into the grounds."
second_door = '''\nYou open the door and Mr. Filch is standing right there with a satisfied smirk on his face.\n
"Oh my, we are in trouble arent we.",he says as he grabs you by the cloak and takes you to Professor Snape who gives you a months worth of detention.\n
GAME OVER'''
second_stairs="\nYou climb the stairs and get to the second floor landing.  You can either keep climbing to the third floor or go down the hallway to your right."
third_up="\nYou know the third floor corridor is off limits to students!  You run into Fluffy who you spend the rest of the night running away from.\nGAME OVER"
third_right='''\nYou walk down the hallway. You heard that Professor Flitwick was keeping hold of TriWizard cup until the start of the TriWizard Tournament.
You try to remember what his office looks like but in the dark its hard to tell.  You stand in front of two doors but you don't remember which is the correct one. '''
fourth_l='''\nYou open the door and out flies a bunch of Cornish Pixies who proceed to lift you up and hang you from a light fixture where you hang until morning.
Professor McGonagall finds you along with a croud of laughing students.  She gets you down while looking very dissapointed and gives you detention and took 15 points away from your house.
GAME OVER.'''
fourth_r='''\nYou chose correctly and enter Professor Flitwicks office.  You look around at all the place he could be hiding it. A few places stick out that you might want to try first.
There is a Wardrobe, a Small Chest, and a curtain blocking something that seems to be glowing blue.'''
final_wardrobe='''\nYou open the Wardrobe and out climbs a huge clown with a white face with red makeup wearing a frilled clown outfit and holding a red baloon on a string.
On the balloon it says "You'll Float Too!". It's a boggart taken the shape of the thing you're most afraid of!
You run screeming from the office and spend the rest of the night curled up on your bed under the covers saying "It wasn't real", again and agin to yourself.
GAME OVER'''
final_curtain='''\nYou pull the curtain to the side revealing a glowing blue orb.  You can't take your eyes off of it and feel this pull towards it and can't help but touch it with your finger.
As soon as your finger touches the surface you are instantly teleported 10 feet above the middle of the black lake. You drop into the cold water and come up spluttering.
Luckily the Giant Squid is near by and picks you up and carries you over to the shore near the castle.
All the while you hear a deep rumbling that sounds like the squid is chuckling to itself.  You walk back up to the castle soaking wet and have to wait to morning to be let in again.
GAME OVER'''
final_chest='''\nYou walk over to the chest thinking it's too small to hold the cup but you also think to your self that Flitwick is the charms teacher.
Congratulations!!! You found the TriWizard cup!! The chest clearly had an undetectable expansion charm placed on it to hold the much bigger cup.
Unfortunately, you can't take it out because it apparently has another charm on it keeping it stuck to the bottom of the chest.
Oh well at least you didn't get caught and get detention or worse!
YOU WIN!!!'''
final_somewhere_else='''\nYou start checking other places and eventually come accross a small locket. You pick it up and open it out of curiosity.
As soon as you open it all the way, you feel your whole body go stiff as the "Patrificus Totalus" jinx is placed on you.
You spend the night frozen there looking at yourself in the tiny mirror it contained all the while the locket keeps emiting a "HA HA" sound
that you think you remeber hearing on a muggle tv show about a yellow colored family with a boy with spiky hair who was always saying "Don't have a cow man!", whatever that means.
GAME OVER'''

# first = input("Which door do you choose, Front or Behind? F or B: ").lower()
# if first == "f":
#     print(first_front)
# elif first == "b":
#     print(first_back)
#     second = input("Which way do you choose? Stairs or Door: ").lower()    
#         if second == "door":
#             print(second_door)
#         elif:first == "b":
#             print(second_stairs)
#             third = input("Which do you choose? Up or Right: ").lower()
#                 if third == "up":
#                     print(third_up)
#                 elif third == "right"
#                     print(third_right)
#                     fourth = input("Which door do you choose, the door on the right or the door on the left? R or L: ").lower()
#                         if fourth == "right"
#                             print(fourth_r)
#                         elif fourth == "l"
#                             print(fourth_l)
#                             final = input("Which do you choose? Wardrobe, Chest, Curtain, or Somewhere else: ").lower
#                                 if final == "chest"
#                                     print(final_chest)
#                                 elif final == "curtain"
#                                     print(final_curtain)
#                                 elif final == "wardrobe"
#                                     print(final_wardrobe)
#                                 elif final == "Somewhere else"
#                                     print(final_somewhere_else)
#                                     
#                         
#                 
#         
# else:
#     print(confused)
first = input("Which door do you choose, Front or Behind? F or B: ").lower()
if first == "f":
  print(first_front)
elif first == "b":
  second = input(first_back + "\nWhich way do you choose? Stairs or Door: ").lower()
  if second == "door":
    print(second_door)
  elif second == "stairs":
    third = input(second_stairs + "\nWhich do you choose? Up or Right: ").lower()
    if third == "up":
        print(third_up)
    elif third == "right":
        fourth = input(third_right + "\nWhich door do you choose, the door on the right or the door on the left? R or L: ").lower()
        if fourth == "l":
            print(fourth_l)
        elif fourth == "r":
            final = input(fourth_r + "\nWhich do you choose? Wardrobe,Chest,Curtain,or Somewhere_else: ").lower()
            if final == "wardrobe":
                print(final_wardrobe)
            elif final == "chest":
                print(final_chest)
            elif final == "curtain":
                print(final_curtain)
            elif final == "somewhere else":
                print(final_somewhere_else)
            else:
                print(confused)
        else:
            print(confused)
    else:
        print(confused)    
else:
  print(confused)
  
#     if third == "up":
#         print(third_up)
#       elif third == "right":
#         print(third_right)
#       fourth = input("Which door do you choose, the door on the right or the door on the left? R or L: ").lower()
#           if fourth == "r":
#             print(fourth_r)
#           elif fourth == "l":
#             print(fourth_l)
#           final = input("Which do you choose? Wardrobe, Chest, Curtain, or Somewhere else: ").lower
#               if final == "wardrobe":
#                 print(final_wardrobe)
#               elif final == "chest":
#                 print(final_chest)
#               elif final == "curtain":
#                 print(final_curtain)
#               elif final == "somewhere else":
#                 print(final_somewhere_else)
#             