import random
mylist = ["Mcdoanlds", "Burger King", "In n Out"]
print(mylist)
r = random.randrange(3)
x = input("choose a restaurant:" )
if x == "Mcdoanlds":
    print("Heres the menu")
    print("burger,fries,mcnuggets")
elif x == 'Burgur king':
    print("Heres the menu")
    print("Shake,burger,fries,nuggets")
elif x == 'In n Out':
    print("Heres the menu")
    print("Shake,burger,animal sytle fries")
print(r)
    


