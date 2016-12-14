"""
         The 2048 Game
Deveoper :   Vipul Chasta
Contact No:  +91 7737770002
e-mail ID:   chasta.vipul@gmail.com
Data:        15-12-2016
Description: Simple Board Game
"""

# Matrix Creation and Initialization
matrix = []
for i in range(0,4):
    matrix.append([])
    for j in range(0,4):
        matrix[i].append(0)


#Import Statements
import random

print("Welcome to 2048 Game.")

