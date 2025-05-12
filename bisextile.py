# Os variables import for windows
import os

# Script that check if a year is besextile

# Wait for user input year
annee = input("Saisissezune année: ")
annee = int(annee)

if annee % 400 ==0 or (annee % 4 ==0 and annee % 100 != 0):
    print("L'anne saisie est bisextile.")

else:
    print("L'année saisie n'est pas bisextile.")

os.system("pause")