'''
Rock, Paper, Scissors Game

Make a rock-paper-scissors game where it is the player vs the computer.
The computer’s answer will be randomly generated, while the program will
ask the user for their input. This project will better your understanding
of while loops and if statements.

'''
import random
print("Rock, Paper, Scissors Game \n , how many turn you want to play :")
turns=int(input())

computer=["Rock", "Paper", "Scissors"]

user={  "Rock":["Paper", "Scissors"],
        "Paper":["Rock", "Scissors"],
        "Scissors":["Paper" , "Rock"]}



win =0
loss=0
tie=0 

i=0
while i < turns : 
    print("please choose 1>Rock , 2>Paper , 3>Scissor ")
    userInput=int(input())
    userchoice=computer[userInput-1]
    computerInput=random.randint(0,2)
    computerchoice=computer[computerInput]

    if userchoice == computerchoice :
        tie+=1
        print("computer choose : ",computerchoice)
        print("no one win")
    elif user[userchoice][0] == computerchoice:
        win+=1
        print("computer choose : ",computerchoice)
        print("you win")
    else:
        loss+=1
        print("computer choose : ",computerchoice)
        print("computer win ")

    
    i+=1

print(" Results \n ------------- ")
print("wins : ",win,"\n -------------")
print("loss : ",loss,"\n -------------")
print("tie : ",tie,"\n -------------")



    