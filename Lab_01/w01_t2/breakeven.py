item_cost = 20.0  #Cost to produce each item
sale_price = 40.0 #The sale price per item (item cost + profit per item) 
fixed_costs = 50000.00 #Fixed costs
profit = sale_price-item_cost
break_even = (fixed_costs/(profit)) #Break even

#print out 
print("Cost to produce each item:", item_cost)
print("Sale price for each item:", sale_price)
print("Fixed costs:", fixed_costs)
print("Profit per item:", profit)
print("Break even:", break_even, "items")


