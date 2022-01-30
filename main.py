from random import choice
from os import system

while True: # Main Loop

    user_input=input("User input: ")
    user_input=user_input.upper()
    comp_choice=choice(['R','P','S'])

    print(comp_choice)

    if user_input=='R' and comp_choice=='S':
        print("You win")

    elif user_input=='P' and comp_choice=='S':
        print("You lose")

    elif user_input=='S' and comp_choice=='S':
        print("Match draw")
    

    elif user_input=='S' and comp_choice=='P':
        print("You win")
            
    elif user_input=='R' and comp_choice=='P':
        print("You lose")

    elif user_input=='P' and comp_choice=='P':
        print("Match draw")

    
    elif user_input=='P' and comp_choice=='R':
        print("You win")

    elif user_input=='S' and comp_choice=="R":
        print("You lose")
    
    elif user_input=='R' and comp_choice=="R":
        print("Match draw")


    else:
        print("Please enter a valid input (R, P, S)")
