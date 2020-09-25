# Uncertain_Reward.py
# Created by: James McKenzie
# Created on: 20/08/2020
# Last modified on: 25/09/2020

''' Version: 4 (final version)
    This is the final, fully completed version of the program
'''

import random
import time

BASE_REWARD = 5
ERROR = "Invalid input!"
LIVES = 3
BONUS = 50





def find_factors(num):
    '''This function is used for division problems.
       It finds the factors of the first chosen number,
       then compiles them into a list and returns it.
       The second number in division problems is randomly
       chosen from this list
    '''

    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors
        

def questions(difficulty):

    questions_list = []
    numbers_list = []
    counter = 0

    qs = 0

    ms = 0

    if difficulty == "e":
        qs = 9

    elif difficulty == "n" or difficulty == "h":
        qs = 5

    if difficulty == "n":
        ms = 4

    elif difficulty == "h":
        ms = 5
    
    if difficulty == "n":
        ds = 3

    elif difficulty == "h":
        ds = 4
    
    if difficulty == "e" or difficulty == "n":
        for i in range(1,qs):
            problem = []
            num1 = random.randint(50,100)
            num2 = random.randint(1,50)
            question = "What is {} plus {}?".format(num1, num2)
            if question not in numbers_list:
                problem.append(question)
                answer = num1 + num2
                problem.append(answer)
                questions_list.append(problem)
            numbers_list.append(question)

        for i in range(1,qs):
            problem = []
            num3 = random.randint(50,100)
            num4 = random.randint(1,50)
            question = "What is {} minus {}?".format(num3, num4)
            if question not in numbers_list:
                problem.append(question)
                answer = num3 - num4
                problem.append(answer)
                questions_list.append(problem)
            numbers_list.append(question)

    if difficulty == "n" or difficulty == "h":
        for i in range(1,ms):
            problem = []
            num5 = random.randint(2,12)
            num6 = random.randint(2,12)
            question = "What is {} times {}?".format(num5, num6)
            if question not in numbers_list:
                problem.append(question)
                answer = num5 * num6
                problem.append(answer)
                questions_list.append(problem)
            numbers_list.append(question)

        while counter < ds:
            problem = []
            num7 = random.randint(6,50)
            factors = find_factors(num7)
            num8 = random.choice(factors)
            if num8 > 1 and num8 < num7:
                question = "What is {} divided by {}?".format(num7, num8)
                if question not in numbers_list:
                    problem.append(question)
                    answer = num7 / num8
                    problem.append(answer)
                    questions_list.append(problem)
                    counter += 1
                numbers_list.append(question)

    
            
    return questions_list

def word_questions(difficulty):

    names_list = ["Johnny", "Sarah", "Mohammed", "Ruby", "Tane", "Maia"]

    questions = []


    while True:
        problem = []
        name = random.choice(names_list)
        num1 = random.randint(50,100)
        num2 = random.randint(1,50)
        question = "{} has {} dollars in their bank account. Every week they get paid {} dollars as an allowance.\nHow much money is now in their account?".format(name, num1, num2)
        problem.append(question)
        answer = num1 + num2
        problem.append(answer)
        questions.append(problem)
        break

    while True:
        problem = []
        name = random.choice(names_list)
        num1 = random.randint(50,100)
        num2 = random.randint(1,50)
        question = "{} is picking berries. They have picked {} so far and need to pick {} more to sell them as a bag\nHow much berries are in one bag?".format(name, num1, num2)
        problem.append(question)
        answer = num1 + num2
        problem.append(answer)
        questions.append(problem)
        break

    while True:
        problem = []
        name = random.choice(names_list)
        num1 = random.randint(50,100)
        num2 = random.randint(1,50)
        question = "{} has {} sweets. They give {} to a friend as payment for a good deed.\nHow many sweets do they have now?".format(name, num1, num2)
        problem.append(question)
        answer = num1 - num2
        problem.append(answer)
        questions.append(problem)
        break

    while True:
        problem = []
        name = random.choice(names_list)
        num1 = random.randint(50,100)
        num2 = random.randint(1,50)
        question = "{} is raising money to go on a school trip. They've raised ${} so far and the fee for the trip is ${}.\nHow much money do they still need to raise?".format(name, num2, num1)
        problem.append(question)
        answer = num1 - num2
        problem.append(answer)
        questions.append(problem)
        break

    if difficulty == "n":
    
        while True:
            problem = []
            name = random.choice(names_list)
            num1 = random.randint(2,12)
            num2 = random.randint(2,12)
            question = "{}'s pond is infested with algae. A week ago the area of the algae was {} square metres.\nSince then it has multiplied by {}. What is the area of the algae now?".format(name, num1, num2)
            problem.append(question)
            answer = num1 * num2
            problem.append(answer)
            questions.append(problem)
            break

        while True:
            problem = []
            name = random.choice(names_list)
            num1 = random.randint(6,50)
            factors = find_factors(num1)
            num2 = random.choice(factors)
            if num2 > 1 and num2 < num1:
                question = "{} is planning a party.\nThey have enough money to buy {} drinks and have decided each guest is entitled to at least {} drinks.\nWhat is the maximum number of guests that can attend the party?".format(name, num1, num2)
                problem.append(question)
                answer = num1 / num2
                problem.append(answer)
                questions.append(problem)
                break

    return questions

def decimals():

    questions = []
    numbers_list = []


    for i in range(1,3):
        problem = []
        num1 = round(random.uniform(10.1, 24.9), 1)
        num2 = round(random.uniform(0.1, 10.1), 1)
        question = "What is {} plus {}?".format(num1, num2)
        if question not in numbers_list:
            problem.append(question)
            answer = round((num1 + num2),1)
            problem.append(answer)
            questions.append(problem)
        numbers_list.append(question)

    for i in range(1,3):
        problem = []
        num1 = round(random.uniform(10.1, 24.9), 1)
        num2 = round(random.uniform(0.1, 10.1), 1)
        question = "What is {} minus {}?".format(num1, num2)
        if question not in numbers_list:
            problem.append(question)
            answer = round((num1 - num2),1)
            problem.append(answer)
            questions.append(problem)
        numbers_list.append(question)

    return questions

def fracts():

    questions = []
    numbers_list = []

    names_list = ["Johnny", "Sarah", "Mohammed", "Ruby", "Tane", "Maia"]


    for i in range(1,5):
        problem = []
        num1 = random.randint(1,12)
        num2 = random.randint(1,12)
        num3 = random.randint(1,12)
        num4 = random.randint(1,12)
        question = "What is {}/{} times {}/{}?".format(num1, num2, num3, num4)
        if question not in numbers_list:
            problem.append(question)
            answer = "{}/{}".format((num1 * num3), (num2 * num4))
            problem.append(answer)
            questions.append(problem)
        numbers_list.append(question)

    while True:
        problem = []
        name = random.choice(names_list)
        num1 = random.randint(1,6)
        num2 = random.randint(7,12)
        num3 = random.randint(1,12)
        num4 = random.randint(1,12)
        question = "{}'s pond is infested with algae. A week ago the area of the algae was {}/{} of the pond.\nSince then it has multiplied by {}/{}. What is the area of the algae now?".format(name, num1, num2, num3, num4)
        problem.append(question)
        answer = "{}/{}".format((num1 * num3), (num2 * num4))
        problem.append(answer)
        questions.append(problem)
        break

    return questions

def dec_words():

    questions = []
    names_list = ["Johnny", "Sarah", "Mohammed", "Ruby", "Tane", "Maia"]

    while True:
        problem = []
        name = random.choice(names_list)
        num1 = round(random.uniform(10.1, 24.9), 1)
        num2 = round(random.uniform(0.1,10.1), 1)
        question = "{} has ${:.2f} in their bank account. Every week they get paid ${:.2f} as an allowance.\nHow much money is now in their account? (answer to 1dp)".format(name, num1, num2)
        problem.append(question)
        answer = round((num1 + num2),1)
        problem.append(answer)
        questions.append(problem)
        break

    while True:
        problem = []
        name = random.choice(names_list)
        num1 = round(random.uniform(10.1, 24.9), 1)
        num2 = round(random.uniform(0.1,10.1), 1)
        question = "{} is raising money to go on a school trip. They've raised ${:.2f} so far and the fee for the trip is ${:.2f}.\nHow much money do they still need to raise? (answer to 1dp)".format(name, num2, num1)
        problem.append(question)
        answer = round((num1 - num2),1)
        problem.append(answer)
        questions.append(problem)
        break

    while True:
        problem = []
        name = random.choice(names_list)
        num1 = round(random.uniform(10.1, 24.9), 1)
        num2 = round(random.uniform(0.1,10.1), 1)
        question = "{} is painting a border around a wall. The length of the wall is {} and the width is {}.\nWhat is the perimeter of the wall? (answer to 1dp)".format(name, num1, num2)
        problem.append(question)
        answer = round(((num1 + num2) * 2),1)
        problem.append(answer)
        questions.append(problem)
        break

    

    return questions

    

def gambling(points):
    # Gambling code goes here
   

    

    coin = random.randint(1,2)
    print("This is your chance to earn bonus points! If you win, you earn an extra {} points!\n".format(BONUS))
    print("However, if you lose, you lose ALL your points! Muahaha!\n")
    while True:
        heads_or_tails = input("I have a coin, you pick a side. Heads or tails?").strip().lower()
        if heads_or_tails == "tails":
            if coin == 2:
                print("Result: Tails")
                print("You win!\n")
                points += BONUS
                break
            else:
                print("Result: Heads")
                print("Sorry, you lose!\n")
                points = 0
                break
        elif heads_or_tails == "heads":
            if coin == 1:
                print("Result: Heads")
                print("You win!\n")
                points += BONUS
                break
            else:
                print("Result: Tails")
                print("Sorry, you lose!\n")
                points = 0
                break
        else:
            print("Please enter either 'heads' or 'tails'!\n")

    return points

def hard_gambling(points):

    bonus = BONUS * 2

    spades = ['Ace of Spades', '6 of Spades']
    clubs = ['King of Clubs', 'Jack of Clubs']
    hearts = ['Queen of Hearts', '7 of Hearts']
    diamonds = ['5 of Diamonds', 'Ace of Diamonds']
    suits = [spades, clubs, hearts, diamonds]
    
    print("This is your chance to earn bonus points! If you win, you earn an extra {} points!\n".format(bonus))
    print("However, if you lose, you lose ALL your points! Muahaha!\n")
    time.sleep(2)
    print("Now you may think this is another coin toss, but this is hard mode.\nSo I have another trick up my sleeve!")
    time.sleep(2.5)
    print("I have a pack of cards and I will draw a random card\n")
    print("Pick a suit. If the card I draw is in that suit, you win. If not, you lose all your points!\n")
    s = input("Spades, Clubs, Diamonds or Hearts?").strip().lower()
    if s == "spades":
        suit = random.choice(suits)
        card = random.choice(suit)
        print("Result: {}\n".format(card))
        if suit == suits[0]:
            print("You win!\n")
            points += bonus
        else:
            print("Sorry, you lose!\n")
            points = 0
    elif s == "clubs":
        suit = random.choice(suits)
        card = random.choice(suit)
        print("Result: {}\n".format(card))
        if suit == suits[1]:
            print("You win!\n")
            points += bonus
        else:
            print("Sorry, you lose!\n")
            points = 0
    elif s == "hearts":
        suit = random.choice(suits)
        card = random.choice(suit)
        print("Result: {}\n".format(card))
        if suit == suits[2]:
            print("You win!\n")
            points += bonus
        else:
            print("Sorry, you lose!\n")
            points = 0
    elif s == "diamonds":
        suit = random.choice(suits)
        card = random.choice(suit)
        print("Result: {}\n".format(card))
        if suit == suits[3]:
            print("You win!\n")
            points += bonus
        else:
            print("Sorry, you lose!\n")
            points = 0
        
    else:
        print("Please enter either 'spades', 'clubs', 'hearts' or 'diamonds'!\n")

    return points
        
def test(difficulty):
    # Overall routine goes here

    problems = questions(difficulty)
    word_problems = word_questions(difficulty)
    decs = decimals()
    fractions = fracts()
    hard_words = dec_words()

    gain = 0
    if difficulty == "h":
        gain = (BASE_REWARD * 2)
    else:
        gain = BASE_REWARD

    score = 0

    for i in range(len(problems)):
        while True:
            try:
                answer = int(input(problems[i][0]))
                if answer == problems[i][1]:
                    print('Correct!\n')
                    score += gain
                    print("Points Gained: {}\n".format(gain))
                    break
                else:
                    print("WRONG!\n")
                    break

            except ValueError:
                print(ERROR)
    if difficulty == "h":

        for i in range(len(decs)):
            while True:
                try:
                    answer = float(input(decs[i][0]))
                    if answer == decs[i][1]:
                        print('Correct!\n')
                        score += gain
                        print("Points Gained: {}\n".format(gain))
                        break
                    else:
                        print("WRONG!\n")
                        break

                except ValueError:
                    print(ERROR)
        
        for i in range(len(fractions)):
            while True:
                answer = input(fractions[i][0])
                if answer == fractions[i][1]:
                    print('Correct!\n')
                    score += (gain * 2)
                    print("Points Gained: {}\n".format((gain * 2)))
                    break
                
                else:
                    answer_list = list(answer)
                    if "/" not in answer_list:
                        print(ERROR)
                    else:
                        print("WRONG!\n")
                        break

        for i in range(len(hard_words)):
            while True:
                try:
                    problem = random.choice(hard_words)
                    answer = float(input(problem[0]))
                    if answer == problem[1]:
                        print('Correct!\n')
                        score += (gain * 2)
                        print("Points Gained: {}\n".format(gain * 2))
                        break
                    else:
                        print("WRONG!\n")
                        break

                except ValueError:
                    print(ERROR)

            hard_words.remove(problem)



    if difficulty == "e" or difficulty == "n":
        for i in range(len(word_problems)):
            while True:
                try:
                    problem = random.choice(word_problems)
                    answer = int(input(problem[0]))
                    if answer == problem[1]:
                        print('Correct!\n')
                        score += (gain * 2)
                        print("Points Gained: {}\n".format(gain * 2))
                        break
                    else:
                        print("WRONG!\n")
                        break

                except ValueError:
                    print(ERROR)

            word_problems.remove(problem)
        

    return score
            
def main():

    
    lives = LIVES
    total_score = 0
    achievements = []
    q = False
    g = False

    print("Welcome to MathsKing!\n")
    time.sleep(2.5)
    print("MathsKing is a game where you are asked twenty maths questions per round.")
    print("For every correct answer, you earn points.\n")
    time.sleep(4)
    print("But here's the fun part!")
    time.sleep(2)
    print("At the end of each round you can flip a virtual coin to earn bonus points! Amazing!\n")
    time.sleep(3.5)
    print("BUT, if you lose the coin toss, you lose one of your lives.")
    time.sleep(2)
    print("And if you lose all your lives, well, that only means one thing – GAME OVER!\n")
    time.sleep(3)
    print("So be careful – don't get cocky, or you may lose all your lives.\n")
    time.sleep(3)
    print("Select which difficulty aligns with your maths skills to maximise your score and earn achievements!")
    print("Do you think you’re up to the challenge of HARD MODE?\n")
    time.sleep(3)
    
    print("----------------------------------------------------------------------------------------------------------------------------\n")
    while q == False:
        if total_score != 0:
            print("Achievements Earned:")
            for achievement in achievements:
                print(achievement)
        print("///////////////////////////////////////////////////////////////////////////////")
        print("Type [E] for Easy Mode (Just Addition and Subtraction)")
        print("///////////////////////////////////////////////////////////////////////////////")
        print("Type [N] for Normal Mode (Addition, Subtraction, Multiplication and Division)")
        print("///////////////////////////////////////////////////////////////////////////////")
        print("Type [H] for Hard Mode (Multiplication, Division, Decimals and Fractions)")
        print("///////////////////////////////////////////////////////////////////////////////")
        difficulty = input("Type [Q] to quit").strip().lower()
        if difficulty == "e" or difficulty == "n" or difficulty == "h":

            print("You have {} lives. The test begins...\n".format(lives))
            time.sleep(3)
            print("NOW!\n")
        
            score = test(difficulty)
            highest_score = 0
            if difficulty == "e":
                highest_score = 120
            elif difficulty == "n":
                highest_score = 130
            elif difficulty == "h":
                highest_score = 280
                
            print("Score: {}\n".format(score))

            if score == 0:
                print("Oh no! Better luck next time")

            else:
                while True:
                    gamble = input("Do you want to gamble your winnings? Yes or no").strip().lower()
                    if gamble == "yes":
                        if difficulty == "h":
                            score = hard_gambling(score)
                        else:
                            score = gambling(score)
                        print("Score: {}\n".format(score))
                        g = True
                        break
                    elif gamble == "no":
                        print("Okay then\n")
                        g = False
                        break
                    else:
                        print("Please enter either 'yes' or 'no'!")
            total_score += score

            print("Total Score: {}\n".format(total_score))
            
            if score == 0:
                lives -= 1
            else:
                if score > 0 and g == True:
                    achievement = "I'm Feeling Lucky (won a round of gambling)"
                    if achievement not in achievements:
                        print("Achievement Earned! - {}".format(achievement))
                        achievements.append(achievement)
                    if difficulty == "h":
                        achievement = "Luck of the Irish (won a round of gambling on hard mode)"
                        if achievement not in achievements:
                            print("Achievement Earned! - {}".format(achievement))
                            achievements.append(achievement)
                if score >= highest_score:
                    achievement = "Maths King (passed a round without any wrong answers)"
                    if achievement not in achievements:
                        print("Achievement Earned! - {}".format(achievement))
                        achievements.append(achievement)
                    if difficulty == "h":
                        achievement = "Maths Queen (passed a round of hard mode without any wrong answers)"
                        if achievement not in achievements:
                            print("Achievement Earned! - {}".format(achievement))
                            achievements.append(achievement)
                if score >= highest_score and g == True and difficulty == "h":
                    achievement = "Maths Emperor (passed hard mode with no wrong answers and won the gamble)"
                    if achievement not in achievements:
                        print("Achievement Earned! - {}".format(achievement))
                        achievements.append(achievement)
                if total_score >= 300:
                    achievement = "Maths Lord (accrued a total score of 300 or more)"
                    if achievement not in achievements:
                        print("Achievement Earned! - {}".format(achievement))
                        achievements.append(achievement)
                if total_score >= 500:
                    achievement = "Maths Warrior (accrued a total score of 500 or more)"
                    if achievement not in achievements:
                        print("Achievement Earned! - {}".format(achievement))
                        achievements.append(achievement)
                if total_score >= 1000:
                    achievement = "Maths God (accrued a total score of 1000 or more)"
                    if achievement not in achievements:
                        print("Achievement Earned! - {}".format(achievement))
                        achievements.append(achievement)
                

            print("Lives: {}\n".format(lives))

            if lives == 0:
                print("GAME OVER")
                q = True

            q = False

        elif difficulty == "q":
            print("Okay then.\n")
            q = True
        else:
            print("Please type either 'e', 'n', 'h', or 'q'!\n")

    print("----------------------------------------------------------------------------------------------------------------------------\n")
    print("Thank you for playing MathsKing!")
    print("MathsKing was developed by James McKenzie in 2020.")
    print("If you have any questions, feedback or have found any bugs, feel free to contact me at \njames.mckenzie@student.onslow.school.nz")
        

main()
                
    

    
