import os
import sys
import math

def table(nb,max=10):
    """This function will display multiplication table by nb for 1*nb to max*nb
    
    (max >=0)"""
    i=0 
    while i< max:
        print(i+1,"*",nb,"=",(i+1)*nb)
        i += 1

def carre(variable):
    """Returns square value"""
    return(variable*variable)

def use_lambda():
    """how to use lambda"""
    f = lambda x: x*x
    g = f*(lambda y : y*y)
    return f,'ahaha',g 

def sqrt(nb):
    """Use math import library sQRT """
    return math.sqrt(nb)

if __name__=='__main__':
    #table(3)
    #variable = carre(-5)
    #print(variable)
    # try lambda
    f = lambda x: x*x
    print(sqrt(4))
    help("math.sqrt")



