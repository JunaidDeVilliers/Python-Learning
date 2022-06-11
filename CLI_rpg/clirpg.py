
# Save the user input options you allow e.g. in a set that you can check against when your user makes a choice.
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending on what items they have 
# in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random 
# element can have an effect on whether your player wins or loses when battling an opponent.


from random import randint


name = input("Enter your character name: ")
print("Welcome " + name + " to my Text Adventure")

player_actions = {"door": None, "playing": True, "choice": None}
inventory = {}

while player_actions["playing"] == True:

    # First while loop to make sure user selects a valid door. Will repeat until valid answer is given
    while player_actions["door"] != "left" and player_actions["door"] != "right" and player_actions["door"] != "middle":
        player_actions["door"] = input("You see 3 doors ahead will you go left, right or middle: ")
        
        if player_actions["door"] == "left":

            # checking to see if user already searched the left room and found the sword
            if "sword" in inventory:
                print("You investigate the left room again and find nothing so you return")
                player_actions["door"] = None
                continue
            print("You have chosen the left door")
        elif player_actions["door"] == "right":
            print("You have chosen the right door")
        elif player_actions["door"] == "middle":
            print("You have chosen middle door")
            if "sword" in inventory and inventory["sword"] == "Infused sword":
                print("You investigate the middle room again and find nothing so you return")
                player_actions["door"] = None
                continue
            elif "gem" in inventory and inventory["gem"] == "Powergem":
                print("You investigate the middle room again and find nothing so you return")
                player_actions["door"] = None
                continue
        else:
            print("Invalid input. Please input only left or right")
    
    # actions for when user chose the left door
    if player_actions["door"] == "left":
        while player_actions["door"] == "left":
            player_actions["choice"] = input("You arrive at an empty room, you can either search or go back? ")
            
            if player_actions["choice"] == "search" and "gem" in inventory and inventory["gem"] == "Powergem":
                print("All you find is a regular sword, you pick it up and infuse your powergem into it creating an infused sword")
                print("You go back")
                inventory["sword"] = "Infused sword"
                player_actions["door"] = None
            elif player_actions["choice"] == "search":
                print("All you find is a regular sword, you pick it up and go back")
                inventory["sword"] = "Regular sword"
                player_actions["door"] = None
            elif player_actions["choice"] == "back":
                player_actions["door"] = None
            else:
                print("invalid choice. Please choose search/back")
    
    # actions for when user chose the middle door
    elif player_actions["door"] == "middle":
        while player_actions["door"] == "middle":
            player_actions["choice"] = input("You arrive at an empty room, you can either search or go back? ")
            
            if player_actions["choice"] == "search" and "sword" in inventory and inventory["sword"] == "Regular sword":
                print("You find a powergem that can be infused in your sword, you infuse your sword and go back")
                inventory["sword"] = "Infused sword"
                player_actions["door"] = None
            elif player_actions["choice"] == "search":
                print("You find a powergem that can be used to infuse a weapon, you pick it up and go back")
                inventory["gem"] = "Powergem"
                player_actions["door"] = None
            elif player_actions["choice"] == "back":
                player_actions["door"] = None
            else:
                print("invalid choice. Please choose search/back")

    # actions for when user chose the right door
    elif player_actions["door"] == "right":
        while player_actions["door"] == "right":
            player_actions["choice"] = input("You encounter a dragon, you can either fight it or go back? ")
            
            # if you fight the dragon with the sword you win, otherwise you lose
            if player_actions["choice"] == "fight":
                odds = randint(1, 30)
                if "sword" in inventory and inventory["sword"] == "Regular sword":
                    if odds > 15:
                        print(f"You use the {inventory['sword']} to beat the dragon")
                        print("You have won the game")
                    else:
                        print(f"Your {inventory['sword']} was not enough to win the fight")
                        print("game over")
                    player_actions["door"] = None
                    player_actions["playing"] = False
                elif "sword" in inventory and inventory["sword"] == "Infused sword":
                    if odds > 5:
                        print(f"You use the {inventory['sword']} to beat the dragon")
                        print("You have won the game")
                    else:
                        print(f"Your {inventory['sword']} was not enough to win the fight")
                        print("game over")
                    player_actions["door"] = None
                    player_actions["playing"] = False
                else:
                    print("You fail to slay the dragon empty handed")
                    print("You are killed. Game over")
                    player_actions["door"] = None
                    player_actions["playing"] = False
            elif player_actions["choice"] == "back":
                player_actions["door"] = None
            else:
                print("invalid choice. Please choose search/back")

    #incase an unkown error occurs
    else:
        print("An unkown error occurred")