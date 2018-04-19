# create game to guess a word from list
# a
text="overnight"
characters=list(text)
print(*characters,sep=", ")
from random import choice
for i in range(len(characters)):
    n=choice(characters)
    characters.remove(n)
    print(n,end=" ")
print()
count=0
while count<3:
    a=input("Your anser: ")
    if a==text:
        print("Hura!!")
        break
    else:
        print("Guess again...:(")
        count+=1
if count==3:
    print("Game over!!")
