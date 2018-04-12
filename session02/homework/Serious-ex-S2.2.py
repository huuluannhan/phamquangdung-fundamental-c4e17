n=int(input("Chose your positive integer number: "))
S=1
P=0
if n<0:
    print("No result for negative integer")
elif n==0:
    print("The factorial of your number: ",S)
    print("Error to check your sum of harmonic number")
else:
    for i in range(1,n,1):
        S=S*i
        P=P+1/i
    print("The factorial of your number: ",S)
    print("Your string of harmonic number is: ",P)
