

numItems = int(input("how many items? "))
total = 0
for i in range(0,numItems):
    item = input("Whats the item? ")
    price = float(input("whats the price "))
    print("Thanks for buying " + item)
    total = total + price 
print("Your total is: " + str(total))
    
    

