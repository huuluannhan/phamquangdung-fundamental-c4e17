a=input(("Welcome to our shop, what do you want(C,R,U,D): "))
shops=["T-shirt","Sweater"]
if a=="R":
    print("Our item: ",end="")
    print(*shops,sep=", ")
    a=input(("Welcome to our shop, what do you want(C,R,U,D): "))
    if a=="C":
        n=input("Enter new item: ")
        shops.append(n)
        print("Our item: ",end="")
        print(*shops,sep=", ")
        a=input(("Welcome to our shop, what do you want(C,R,U,D): "))
        if a=="U":
            p=int(input("Update position: "))-1
            shops[p]=input("New item: ")
            print("Our item: ",end="")
            print(*shops,sep=", ")
            a=input(("Welcome to our shop, what do you want(C,R,U,D): "))
            if a=="D":
                p=int(input("Delete position: "))-1
                shops.pop(p)
                print("Our item: ",end="")
                print(*shops,sep=", ")
else:
    print("Please choose your act again!")
