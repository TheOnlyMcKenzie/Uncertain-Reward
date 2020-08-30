# Uncertain_Reward.py
# Created by: James McKenzie
# Created on: 20/08/2020
# Last modified on: 31/08/2020

''' Version: 2.0
    In this version I have set up the base function of what the program should do
    There is a dictionary of example questions, and the user is tested
    In terms of gambling, I have selected one method - a coin toss
    This acts as the current master copy of the code, updated as components are completed
'''

BASE_REWARD = 5
ERROR = "Invalid input!"

# Set up dictionary of example problems
# This will be expanded later

problems_dic = {"What is 6 multiplied by 12?":72,"What is 78 minus 24?":54,"What is 64 divided by 4?":16}


def gambling(points):
    # Gambling code goes here
    import random

    x = 10

    coin = random.randint(1,2)
    print("This is your chance to earn bonus points! If you win, you earn an extra 10 points!\n")
    print("However, if you lose, you lose ALL your points! Muahaha!\n")
    heads_or_tails = input("I have a coin, you pick a side. Heads or tails?").strip().lower()
    if heads_or_tails == "tails":
        if coin == 2:
            print("Result: Tails")
            print("You win!")
            points += x
        else:
            print("Result: Heads")
            print("Sorry, you lose!")
            points = 0
    elif heads_or_tails == "heads":
        if coin == 1:
            print("Result: Heads")
            print("You win!")
            points += x
        else:
            print("Result: Tails")
            print("Sorry, you lose!")
            points = 0
    else:
        print("Please enter either 'heads' or 'tails'!")

    return points

        
def main():
    # Overall routine goes here
    score = 0
    for key, value in problems_dic.items():
        try:
            answer = int(input(key))
            if answer == value:
                print('Correct!\n')
                score += BASE_REWARD
            else:
                print("WRONG!\n")
        except ValueError:
            print(ERROR)
    print("Score: {}\n".format(score))

    if score == 0:
        print("Oh no! Better luck next time")
    else:
        gamble = input("Do you want to gamble your winnings? Yes or no").strip().lower()
        if gamble == "yes":
            new_score = gambling(score)
            print("Score: {}\n".format(new_score))
        elif gamble == "no":
            print("Okay then\n")
        else:
            print("Please enter either 'yes' or 'no'!")
            
        

main()
                
    

    
