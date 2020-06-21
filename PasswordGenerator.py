'''
Password Generator

Write a programme, which generates a random password for the user.
Ask the user how long they want their password to be,
and how many letters and numbers they want in their password.
Have a mix of upper and lowercase letters, as well as numbers and symbols.
The password should be a minimum of 6 characters long.
'''
import random 
import string

def genratePass(charlong,numberlong,longPass):

    letters = string.ascii_letters + string.punctuation + string.digits
    num="0123456789"
    charpass = ''.join(random.choice(letters) for i in range(charlong))
    numberpass = ''.join(random.choice(num) for i in range(numberlong))
    
    Password = charpass+numberpass
    FinalPassword = ''.join(random.choice(Password) for i in range(longPass))
    return FinalPassword



print(" welcome to password genreter ")

print("Please Enter Password long :  ")
longPass=int(input())

while longPass < 6 :
    print("Please Enter Password long minimum 6 char : ")
    longPass=int(input())
else:
    print("how many char do you want ?")
    charlong = int(input())
    print("how many number do you want ?")
    numberlong = int(input())

    while numberlong+charlong > longPass :
        print("how many char do you want ? (dont forget your Password long is : )",longPass)
        charlong = int(input())
        print("how many number do you want ? (dont forget your Password long is : )",longPass)
        numberlong = int(input())
    
    else:
        password = genratePass(charlong,numberlong,longPass)
        print("password is :",password)









