from random import randint

# In this part I use (RANDINT METHOD) to generate random number from 0 - 9 for the (3 random Digit) for the result of the BET.
result_bet_1 = randint(0, 9)
result_bet_2 = randint(0, 9)
result_bet_3 = randint(0, 9)

# In this part I assign 1 Variable for the result_bet_1 to result_bet_3 in LIST.
result_of_the_bet = [result_bet_1, result_bet_2, result_bet_3]

# In this part I want to Print the (3 Random Digit) to know what is the combination of the random numbers.
#print(f"The result is:  {result_of_the_bet}  ").

# In this part I create While Loop to repeat the execution.
while True:

# In this part I create (INPUT FUNCTION) to ask the user to ENTER the DESIRED number from 0 - 9 with 3 combination number. 
    bet_1 = int(input("Enter your desired Number for Swertres: "))
    bet_2 = int(input("Enter your desired Number for Swertres: "))
    bet_3 = int(input("Enter your desired Number for Swertres: "))

# In this part I assign 1 Variable for the user's BET from bet_1 - bet_2.
    bet_numbers = [bet_1, bet_2, bet_3]

# In this part I create If Conditional Statement to check if the User's Input from 0 - 9 and if it's return True it print's the results of the (3 random DIgit)
    if not (0 <= bet_1 <= 9 and 0 <= bet_2 <= 9 and 0 <= bet_3 <= 9):
        print("Invalid Input, Try Again")
        continue
    print(f"Result Numbers:  {result_of_the_bet}  ")

# In this part i create If condition to know if the users Win, Partially Win or Lose.
    if bet_numbers == result_of_the_bet:
        print("Congratulations! You Win")
    elif sorted(bet_numbers) == sorted(result_of_the_bet):
        print("Congratulations! You Partially Win")
    else:
        print(f"Sorry you lose! The Result is:  {result_of_the_bet}  ")