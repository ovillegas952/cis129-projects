"""
Author:Omar Villegas
Professor:Troy Adams
Course:CIS 129 
Description:
Coffee Shop Simulator that prints a reciept once the user inputs an amount.
"""
# get user input
num_of_coffees = input("How many coffees would you like?\n")

# get user input
num_of_muffins = input("How many muffins would you like?\n")

# get user input
num_of_sandwiches = input("How many sandwiches would you like?\n")

# get user input
num_of_chocolates= input("How many pieces of chocolate would you like?\n")

# prices 
coffee_price = 5

muffin_price = 4

sandwich_price = 7

chocolate_price = 2

tax = 0.06

# calculate total cost
total_coffee = coffee_price * int(num_of_coffees)
total_muffin = muffin_price * int(num_of_muffins)
total_sandwich = sandwich_price * int(num_of_sandwiches)
total_chocolate = chocolate_price * int(num_of_chocolates)

# calculate taxes
subtotal = total_coffee + total_muffin + total_sandwich + total_chocolate
new_tax = subtotal * tax

total = subtotal + new_tax

# display reciept
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(num_of_coffees)
print("Number of muffins bought?")
print(num_of_muffins)
print("Number of sandwiches bought?")
print(num_of_sandwiches)
print("Number of chocolates bought?")
print(num_of_chocolates)
print("***************************************")
print()
print()
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(str(num_of_coffees) + " Coffee at $" + str(coffee_price) + " each: $ %.2f" % total_coffee)
print(str(num_of_muffins) + " Muffins at $" + str(muffin_price) + " each: $ %.2f" % total_muffin)
print(str(num_of_sandwiches) + " Sandwiches at $" + str(sandwich_price) + " each: $ %.2f" % total_sandwich)
print(str(num_of_chocolates) + " Chocolates at $" + str(chocolate_price) + " each: $ %.2f" % total_chocolate)
print( "6% tax: $" +  str(new_tax))
print("---------")
print("Total: $", total)
print("***************************************")
print("Thank you for supporting a small business!\n")
