import random

print("welcome to Rock Paper Scissors game")
print("Here are the rules of the game")
print("Rock beats Scissors")
print("Paper beats Rock")
print("Scissors beats Paper")
print("if both players have same pick, it's a Tie")

choice = True

while choice:
    possible_options=["Rock", "Papers", "Scissors"]
    player_choice= input("which one will you like to select? (rock, papers, scissors)\n").upper()
    computer_choice = random.choice(possible_options)
        
    print("Player:({})  CPU:({})" .format(player_choice, computer_choice))

    #print('CPU: (%a)' %computer_choice)

    print("Checking both player's moves:")

    if player_choice == "ROCK" and computer_choice == possible_options[2]:
        print("Player wins")
        break
    if computer_choice == possible_options[0] and player_choice == "Scissors":
        print("CPU wins")
        break

    elif player_choice == possible_options:
        print("Tie")

    elif player_choice == "PAPERS" and computer_choice == possible_options[0]:
        print("Player wins")
        break
    elif computer_choice == possible_options[1] and player_choice == "Rock":
        print("CPU wins")
        break

    elif player_choice == "SCISSORS" and computer_choice == possible_options[1]:
        print("Player wins")
        break
    elif computer_choice == possible_options[2] and player_choice == "Papers":
        print("CPU wins")
        break
            
    else:
        print("not amongst our option. Please try again")       

