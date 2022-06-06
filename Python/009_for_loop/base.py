
symbol = input("Please choose a symbol ")
length = int(input("Please enter a line length "))
line = input("Do you want a horizontal or vertical line? ")

if line == 'horizontal':
    for x in range(0,length):
        print(symbol, end='')
elif line == 'vertical':
    for x in range(0,length):
        print(symbol)

