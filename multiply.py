"""Module that muliply any number"""
import os

def table(nb, max=10):
    """1*nb until max*10"""
    i=0
    while i < max:
        print(i+1,'*',nb,"=",(i+1)*nb)
        i+=1

