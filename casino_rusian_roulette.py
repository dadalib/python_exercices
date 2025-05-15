import random
def user_input():
    try:
        ask_number = int(input("Give me your number  between 1 and 50 : "))
    except ValueError:
        print("You are enter a not interger number")

    return ask_number

def random_number():
    return  random.randrange(1,50)

def check_if_user_win():
    pass


if __name__=='__main__':
    value=user_input()
    random_number=int((random_number()))
    print("random_number : ",random_number)
    

