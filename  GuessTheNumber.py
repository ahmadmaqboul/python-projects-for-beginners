'''
Guess The Number :

Write a programme where the computer randomly generates
a number between 0 and 20. The user needs to guess what
the number is. If the user guesses wrong, tell them their
guess is either too high, or too low. This will get you started with
the random library if you haven't already used it.

'''
import random 
print("Guess The Number \n the computer will randomly generates a number between 0 and 20, and you must to guess it ")

gnumber=random.randint(0,20)
userNumber=int(input())

while userNumber > 20 and type(userNumber) != "<class 'int'>" :
    print("please fill the number from 0 - 20 or int number ")
    userNumber = int(input())

while userNumber != gnumber :
    if userNumber > gnumber :
        print("your number greeter than the number")
        userNumber = int(input())

    else:
        print("your number smaller than the number")
        userNumber = int(input())


else:
    print("you find the number", gnumber)



