import random
x = int(input("How many random numbers? "))
thislist = [1,2,3,4,5,6,7,8,9,0]
for y in range(0,x):
    z = random.randrange(10)
    print(thislist[z])
    