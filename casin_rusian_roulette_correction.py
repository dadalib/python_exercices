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
        number_play = input("Play the number between 0 and 49"):
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
            
