number=[1,6,8,1,2,1,5,6]
n=int(input("Enter a number:"))
# Use count() function
print(n,"appears",number.count(n),"in my list")

#not use count() function
count=0
for i in range(len(number)):
    if n==number[i]:
        count+=1
print(n,"appears",count,"in my list")
