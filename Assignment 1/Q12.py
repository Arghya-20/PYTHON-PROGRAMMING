#If the total selling price of 15 items and the total profit earned on them is input through the
#keyboard, write a program to find the cost price of one item.

total_selling_price=float(input("Total selling price of 15 items      : "))
total_profit =float(input("Total profit earned on 15 items      : "))

total_cost_price=total_selling_price - total_profit
cost_price_per_item= total_cost_price/ 15

print("The cost price of one item is  :",cost_price_per_item)