import random


def checkWon(user, com):
    if user == 0 and com == 0:
        return 0
    if(user == 1 and com == 1):
        return -1
    elif(user == 2 and com == 2):
        return -1
    
    
com = random.randint(0, 2)
user = input("Enter 1 snake . 2 water . 3 gun :- ")

print(f"User have Enter :- {user}")
print(f"Com has enter :- {com}")

a = checkWon(user, com)

if(a == 1):
    print('User Won')
elif(a == -1):
    print('Com won')
else:
    print('Draw')
