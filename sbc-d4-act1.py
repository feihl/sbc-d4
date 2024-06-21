from random import randint

# In this part I assign 2 Variables for the choices (Hayang and Kulob).
choice_1 = "Hayang"
choice_2 = "Kulob"       

# In this part I create While Loop to repeat the execution.
while True:

# In this part I create (INPUT FUNCTION) to ask the user to ENTER Hayang or Kulob.     
    player_1 = input("Enter your Choice 'Hayang' or 'Kulob': ").capitalize()

# In this part I create If Statement if the User Input one of the Choices that i created (Hayang and Kulob) it print the Player Choice and Else Invalid if the User inputed none of the choices.
    if player_1 in [choice_1, choice_2]:
        print(f"Real Player 1: {player_1}")

#In this part I assign 2 variable to Computer 1 and 2 that the Computer randomly Choice 0 or 1, 1 means Hayang and 0 means Kulob.
        computer_player_2 = choice_1 if randint(0, 1) == 1 else choice_2
        computer_player_3 = choice_1 if randint(0, 1) == 1 else choice_2

#In this part it prints the random choice of computer_player_2 and computer_player_3.
        print(f"Computer Player 2: {computer_player_2}")
        print(f"Computer Player 3: {computer_player_3}")

#In this part I create If statement to identify who is the winner.
        if player_1 == computer_player_2 == computer_player_3:
            print("It's a TIE!")
        elif player_1 != computer_player_2 and player_1 != computer_player_3:
            print("Player 1 WINS!")
        elif computer_player_2 != player_1 and computer_player_2 != computer_player_3:
            print("Computer Player 2 WINS!")
        elif computer_player_3 != player_1 and computer_player_3 != computer_player_2:
            print("Computer Player 3 WINS!")
        else:
            print("No one wins >>> Please try again <<<")
    else:
        print("Invalid choice, please enter 'Hayang' or 'Kulob'.")