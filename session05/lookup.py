# person=["Quan",40,"single","Hanoi",2,11]
# print(person)
# Dictionary
dict={
    "ng":"người",
    "any":"anh người yêu",
    "fu!!":"f*ck you, dùng khi chửi nhau",
    "omg":"Oh my god, dùng khi than vãn",
    "stt":"status",
}
print("Our dictionary has: ",*dict.keys(),sep=", ")
for i in range(20):
    print("*",end="")
print()
loop=True
while loop:
    n=input("Your code? ")
    if n in dict:
        print("Translation:",dict[n])
    else:
        a=input()
        dict[n]=input("Provide your translation!")
        print(dict)
    k=input("Do you want to play more? (Y/N)").upper()
    if k=="N":
        break
