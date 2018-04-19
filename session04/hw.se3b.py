# create game to guess a word from list
# b
print("Let play humble jungle!!")
from random import randint
characters=['champion','hexagon','picture','coworker']
r=randint(0,len(characters)-1)
texts=list(characters[r])
answers=str(characters[r])
from random import choice
for i in range(len(texts)):
    n=choice(texts)
    texts.remove(n)
    print(n,end=" ")
print()
count=0
while count<3:
    a=str(input("Your anser: "))
    if a==answers:
        print("Hura!!")
        break
    else:
        print("Guess again...:(")
        count+=1
if count==3:
    print("Game over!!")
