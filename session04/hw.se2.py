from random import *
print('''Guess your number game
Now think of a game from 0 to 100, then press 'Enter'
All you have to do is to answer to my guess
'c' if my guess is correct
's' if my guess is smaller than your number
'l' if my guess is larger than your number
''')
Max=100
Min=0
i=50
while True:
    print("Is ",i,"your correct number? ",end="")
    a=input()
    if a=="s":
        Max=i
        i=(Max+Min)//2
    elif a=="l":
        Min=i
        i=(Max+Min)//2
    elif a=="c":
        print("I knew it")
        break
    else:
        print("You only have 3 options: s,l,c")
