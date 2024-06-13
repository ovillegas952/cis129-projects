"""
Omar Villegas
"""
# get user input
num_of_coffees = input("How many coffees would you like?\n")

# get user input
num_of_muffins = input("How many muffins would you like?\n")

# prices 
coffee_price = 5

muffin_price = 4

tax = 0.06

# display reciept
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(num_of_coffees)
print("Number of muffins bought?")
print(num_of_muffins)
print("***************************************")
print()
print()
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
# calculate total cost
total_coffee = coffee_price * int(num_of_coffees)
total_muffin = muffin_price * int(num_of_muffins)
print(str(num_of_coffees) + " Coffee at $" + str(coffee_price) + " each: $" + str(total_coffee))
print(str(num_of_muffins) + " Muffins at $" + str(muffin_price) + " each: $" + str(total_muffin))
# print out tax
subtotal = total_coffee + total_muffin
new_tax = subtotal * tax
print( "6% tax: $" +  str(new_tax))
print("---------")
total = subtotal + new_tax
print("Total: $", total)
print("***************************************")
