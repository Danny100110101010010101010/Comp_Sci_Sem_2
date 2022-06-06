

symbol = input("Please choose a symbol ")
w = int(input("Whats the box width? "))
h = int(input("Whats the box height? "))

for x in range(0,h):
    for y in range(0,w):
        print(symbol, end='')
    print()
    
