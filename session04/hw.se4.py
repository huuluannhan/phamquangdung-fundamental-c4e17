# part a
# i
print("a.i.")
for i in range(20):
    print(i,end=" ")
print()
# ii
print("a.ii.")
n=int(input("Enter a number:"))
for i in range(0,n,1):
    print(i,end=" ")
print()
# part b
# i
print("b.i.")
for i in range(20):
    if i%2==0:
        print("0",end=" ")
    else:
        print("1",end=" ")
print()
# ii
print("b.ii.")
n=int(input("Enter the total number of 1's and 0's: "))
for i in range(n):
    if i%2==0:
        print("0",end=" ")
    else:
        print("1",end=" ")
print()
# part c
# i
print("c.i.")
for i in range(1,10,1):
    for j in range(1,10,1):
        if (i*j)<10:
            print(i*j,end="  ")
        else:
            print(i*j,end=" ")
    print()
# ii
print("c.ii.")
n=int(input("Enter a number: "))
for i in range(1,n,1):
    for j in range(1,n,1):
        if (i*j)<10:
            print(i*j,end="  ")
        else:
            print(i*j,end=" ")
    print()
# part d
# i
print("d.i.")
for i in range(10):
    if i%2!=0:
        for j in range(10):
            if j%2!=0:
                print("1",end=" ")
            else:
                print("0",end=" ")
        print()
    else:
        for j in range(10):
            if j%2!=0:
                print("0",end=" ")
            else:
                print("1",end=" ")
        print()
# ii
print("d.ii.")
n=int(input("Enter a number: "))
for i in range(n):
    if i%2!=0:
        for j in range(n):
            if j%2!=0:
                print("1",end=" ")
            else:
                print("0",end=" ")
        print()
    else:
        for j in range(n):
            if j%2!=0:
                print("0",end=" ")
            else:
                print("1",end=" ")
        print()
