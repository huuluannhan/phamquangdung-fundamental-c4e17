from turtle import *
for i in range(3,7,1):
    if i%2!=0:
        color("blue")
    else:
        color("red")
    for j in range(i):
        forward(100)
        left(360/i)
mainloop()
