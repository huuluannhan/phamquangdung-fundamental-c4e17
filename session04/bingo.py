from random import *
x=randint(1,100)
i=0
while True:
    n=int(input("Guess my number(1-100): "))
    if n<x:
        print("Too small :()")
        i+=1
    elif n>x:
        print("A little too large :(")
        i+=1
    elif n==x:
        print("Bingo")
        break
    print("You have",8-i,"chances to guess!")
    if i==8:
        print("Game over!!")
        break
