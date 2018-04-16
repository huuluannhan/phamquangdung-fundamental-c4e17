sheeps=[5,7,300,90,24,50,75]
# 2.1
print("Hello, my name is Dung and this is my sheeps size: ")
print(sheeps)
# 2.2
print("Now my biggest sheep has size", max(sheeps), "let's shear it")
# 2.3
default_size=8
m=sheeps.index(max(sheeps))
sheeps[m]=default_size
print("After shearing, hear is my flock: ")
print(sheeps)
# 2.4
for i in range(7):
    sheeps[i]=sheeps[i]+50
print("One month has passed, now here is my flock:")
print(sheeps)
# 2.5
print("part 2.5")
sheeps=[5,7,300,90,24,50,75]
month=int(input("Choose number of months: "))+1
for i in range(month):
    print("MONTH", i)
    for i in range(7):
        sheeps[i]=sheeps[i]+50
    print("One month has passed, now here is my flock:")
    print(sheeps)
    print("Now my biggest sheep has size", max(sheeps), "let's shear it")
    default_size=8
    m=sheeps.index(max(sheeps))
    sheeps[m]=default_size
    print("After shearing, hear is my flock: ")
    print(sheeps)
