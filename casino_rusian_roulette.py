import random
def user_budget():
    try:
        ask_budget = int(input("Give me your budget : "))
    except ValueError:
        print("You are enter a not interger number")

    return ask_budget

def user_input():
    try:
        ask_number = int(input("Give me your number  between 1 and 50 : "))
    except ValueError:
        print("You are enter a not interger number")

    return ask_number

def random_number():
    return  random.randrange(1,50)

def half_budget(budget):
    return int(budget/2) 

def check_if_user_win(user_input,random_value,money_budget):
    if user_input == random_value:
        print("You win")
        
    elif random_value%2==0 and user_input%2 ==0:
        print("Pair : Here is hal of you money")
        new_money_budget= half_budget(money_budget)
        print("Here is your money " ,new_money_budget)
    elif random_value%2!=0 and user_input%2!=0:
        print("Not Pair : Here is hal of you money")
        new_money_budget= half_budget(money_budget)
        print("Here is your money ", new_money_budget)

    else:
    
        print("You loose everything : ", int(money_budget-money_budget))


if __name__=='__main__':
    value_user=user_input()
    print(value_user)
    random_number=int(random_number())
    print(random_number)
    budget = user_budget()
    check_if_user_win(value_user,random_number,budget)

    

