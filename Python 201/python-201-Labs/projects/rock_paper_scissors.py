import random

def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    if hand == 0:
        return "scissor"
    elif hand == 1:
        return "rock"
    elif hand == 2:
        return "paper"

def determine_winner(user, pc):
    if user == pc:
        print(f"You had {user} and the computer had {pc}. It was a DRAW!!")
    elif user == "rock" and pc == "scissor":
        print(f"You had {user} and the computer had {pc}. You WON!!")
    elif user == "paper" and pc == "rock":
        print(f"You had {user} and the computer had {pc}. You WON!!")
    elif user == "scissor" and pc == "paper":
        print(f"You had {user} and the computer had {pc}. You WON!!")
    else:
        print(f"You had {user} and the computer had {pc}. You LOSE!!")

playing = True

while playing == True:
    user_hand = 3
    pc_hand = get_hand(random.randint(0,2))

    while user_hand < 0 or user_hand > 2:
        user_hand = int(input("Enter your choice. \n 0 - scissor \n 1 - Rock \n 2 - Paper \n"))

    user_hand = get_hand(user_hand)
    determine_winner(user_hand, pc_hand)

    keep_playing = input("Do you want to keep playing. y/n: ")
    if keep_playing == "n":
        playing = False

