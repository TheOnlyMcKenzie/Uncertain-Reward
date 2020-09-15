# Uncertain_Reward.py
# Created by: James McKenzie
# Created on: 20/08/2020
# Last modified on: 15/09/2020

''' Version: 3.0
    In this version I have randomised the questions the user is asked in the test
    I have also implemented a life system for gambling
    This acts as the current master copy of the code, updated as components are completed
'''

import random 

BASE_REWARD = 5
ERROR = "Invalid input!"
LIVES = 3



def find_factors(num):

    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors
        

def questions():

    questions_list = []

    counter = 0

    for i in range(1,7):
        problem = []
        num1 = random.randint(50,100)
        num2 = random.randint(1,50)
        question = "What is {} plus {}?".format(num1, num2)
        problem.append(question)
        answer = num1 + num2
        problem.append(answer)
        questions_list.append(problem)

    for i in range(1,7):
        problem = []
        num3 = random.randint(50,100)
        num4 = random.randint(1,50)
        question = "What is {} minus {}?".format(num3, num4)
        problem.append(question)
        answer = num3 - num4
        problem.append(answer)
        questions_list.append(problem)

    for i in range(1,5):
        problem = []
        num5 = random.randint(2,12)
        num6 = random.randint(2,12)
        question = "What is {} times {}?".format(num5, num6)
        problem.append(question)
        answer = num5 * num6
        problem.append(answer)
        questions_list.append(problem)

    while counter < 4:
        problem = []
        num7 = random.randint(6,50)
        factors = find_factors(num7)
        num8 = random.choice(factors)
        if num8 > 1 and num8 < num7:
            question = "What is {} divided by {}?".format(num7, num8)
            problem.append(question)
            answer = num7 / num8
            problem.append(answer)
            questions_list.append(problem)
            counter += 1

    
    return questions_list


def gambling(points):
    # Gambling code goes here
   

    x = 10

    coin = random.randint(1,2)
    print("This is your chance to earn bonus points! If you win, you earn an extra 10 points!\n")
    print("However, if you lose, you lose ALL your points! Muahaha!\n")
    while True:
        heads_or_tails = input("I have a coin, you pick a side. Heads or tails?").strip().lower()
        if heads_or_tails == "tails":
            if coin == 2:
                print("Result: Tails")
                print("You win!")
                points += x
                break
            else:
                print("Result: Heads")
                print("Sorry, you lose!")
                points = 0
                break
        elif heads_or_tails == "heads":
            if coin == 1:
                print("Result: Heads")
                print("You win!")
                points += x
                break
            else:
                print("Result: Tails")
                print("Sorry, you lose!")
                points = 0
                break
        else:
            print("Please enter either 'heads' or 'tails'!")

    return points

        
def test(score):
    # Overall routine goes here

    problems = questions()

    for i in range(len(problems)):
        while True:
            try:
                answer = int(input(problems[i][0]))
                if answer == problems[i][1]:
                    print('Correct!\n')
                    score += BASE_REWARD
                    break
                else:
                    print("WRONG!\n")
                    break

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

    return new_score
            
def main():
    
    lives = LIVES
    score = 0
    q = False
    while q == False:
        start = input("You have {} lives. Do you want to start the test? Yes or no\n".format(lives))
        if start == "yes":
            score = test(score)
            if score == 0:
                lives -= 1
            print("Lives: {}\n".format(lives))
            if lives == 0:
                print("GAME OVER")
                q = True
            q = False
        elif start == "no":
            print("Okay then\n")
            q = True
        else:
            print("Please answer either 'yes' or 'no'\n")
        

main()
                
    

    
