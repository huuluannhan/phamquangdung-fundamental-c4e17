loop=True
i=0
while loop:
    import getpass
    u=input("Username: ")
    p=getpass.getpass("Password: ")
    if u!="C4E":
        print("no such user")
        i+=1
    elif p!="codethechange":
        print("Password is incorrect")
        i+=1
    else:
        print("Welcome")
        loop=False
    if i==3:
        print("You login incorrectly 3 times. End of process")
        loop=False
