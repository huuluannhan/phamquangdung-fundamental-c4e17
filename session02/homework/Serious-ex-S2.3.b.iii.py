n=int(input("Input your number: "))
if n%2==0:
    for i in range(n//2):
        print("*x",end="")
else:
    for i in range(n//2):
        print("*x",end="")
    print("*")
