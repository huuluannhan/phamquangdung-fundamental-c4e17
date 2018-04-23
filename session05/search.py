numbers=[7,-10,2,8,11,200]
n=int(input("Enter a number: "))
count=0
for i in range(len(numbers)):
    if n==numbers[i]:
        print("Your number appears in the list")
        print(n," stays at postion",numbers.index(n),"in the list")
    else:
        count+=1
if count==len(numbers):
    print("Your number doesnt appears in the list")
