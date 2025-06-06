# The Rusian roulette gamei
import os 
from random import randrange
from math import ceil

# Declaration variable de depart
money = 1000
continue_to_play = True

print("Do you want to play with : ", money," Euros")

# Asking until player dont want to play
while continue_to_play:
    
    # Player number to choose
    number_play=-1
    while number_play <0 or number_play > 49:
        number_play = input("Play the number between 0 and 49 : ")
        try:
            number_play= int(number_play)
        except ValueError:
            print("You are not enter a number")
            number_play = -1
            continue
        if number_play <0:
            print("The number is negatif")
        if number_play > 49:
            print("Thenumber is higher than 49")

        budget=0

        while budget <= 0 or budget > money:
            budget = input("How much money you will play : ")

            try:
                budget = int(budget)
            except ValueError:
                print("There is no number")
                budget=-1
                continue
            if budget <=0:
                print("Te number is negaif")
            if budget > money:
                print("You dont have that money to play, you only have  ", money,"$")

        # Time to play the game
        wining_number= randrange(50)
        print("Circle is tourning and the number is  ... : ", wining_number)

        # Player wins or not
        if wining_number == number_play:
            print("Great you win", budget*3,"$")
            money += budget*3

        elif wining_number%2 == number_play%2:
            # Same Color
            budget = ceil(budget*0.5)
            print("You choose the good color,you get ",budget,"$")
            money +=budget

        else:
            print("Sorry you lost and youlost everithing")
            money -= budget

        # If players broke
        if money <=0:
            print("You are broke !, we close the game")
            keep_playing = False

        else:
            # Display money player
            print("You have the acttual budget",money,"$")
            exit = input("Will you like to exit the casino (y/n) ?")

            if exit == 'y'or exit=='Y':
                print("You exit the casino without earns")
                keep_playing=False

os.system("pause")






                



