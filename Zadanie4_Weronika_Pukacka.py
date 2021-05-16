# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:58:18 2021

@author: Weronika
"""

def funkcja(x):
    for i in range(x,-x-1,1):
        if i%2:
            print()
        else:
            print(i)
            
    x=input("Podaj X: ")
    funkcja(int(x))
    