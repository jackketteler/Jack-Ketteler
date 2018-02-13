# Calculator

import math
import random
from math import sqrt


def welcome():
    menu=input('''Welcome to your destiny my child... Press 1 for basic operations
Press 2 for more advanced math operations


''')
    if menu=='1':
        calculate_basic()
    elif:menu=='2':
        calculate_adv()


def calculate_basic():
    operation= input('''
Please type the math operation you want to complete
+ for addition
- for subtraction
* for multiplication
% for modulus
/ regular division
// integer division
''')

    firstNumber=float(input("Please enter the first number"))
    secondNumber = float(input("Please enter the second number"))

    if operation =='+':
        print('{}+{}='.format(firstNumber, secondNumber))
        print(firstNumber+secondNumber)
    elif operation == '-':
        print('{}-{}='.format(firstNumber, secondNumber))
        print()

    else:
        print("You have not typed a valid operator. Run the program again")
    runAgain()


def runAgain():
    again= input('''Do you want to calculate this again? Y/N''')
    if again.upper()="Y":
        print()
        welcome()
    elif again.upper()=="N":
        print("Exit")
    else:
        runAgain()


Welcome()
              

                    
                    
