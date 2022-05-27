# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.

name = input("Enter your character name: ")
print("Welcome " + name + " to my Text Adventure")

# variable to keep track of which door is selected 
door = None

# variable that can start and stop the game
playing = True

# variable to store user choices
choice = None

# variable to check if user has the sword or not
sword = None

while playing == True:

    # First while loop to make sure user selects a valid door. Will repeat until valid answer is given
    while door != "left" and door != "right":
        door = input("You see 2 doors ahead will you go left or right: ")
        
        if door == "left":

            # checking to see if user already searched the left room and found the sword
            if sword == True:
                print("You investigate the left room again and find nothing so you return")
                door = None
                continue
            door = "left"
            print("You have chosen the left door")
        elif door == "right":
            door = "right"
            print("You have chosen the right door")
        else:
            print("Invalid input. Please input only left or right")
    
    # actions for when user chose the left door
    if door == "left":
        while door == "left":
            choice = input("You arrive at an empty room, you can either search or go back? ")
            
            if choice == "search":
                print("All you find is a sword, you pick it up and go back")
                sword = True
                door = None
            elif choice == "back":
                door = None
            else:
                print("invalid choice. Please choose search/back")

    # actions for when user chose the right door
    elif door == "right":
        while door == "right":
            choice = input("You encounter a dragon, you can either fight it or go back? ")
            
            # if you fight the dragon with the sword you win, otherwise you lose
            if choice == "fight":
                if sword == True:
                    print("You use the sword to beat the dragon")
                    print("You have won the game")
                    door = None
                    playing = False
                else:
                    print("You fail to slay the dragon empty handed")
                    print("You are killed. Game over")
                    door = None
                    playing = False
            elif choice == "back":
                door = None
            else:
                print("invalid choice. Please choose search/back")

    #incase an unkown error occurs
    else:
        print("An unkown error occurred")