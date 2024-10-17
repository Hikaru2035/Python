user = [(input(f"Enter {i+1} items:"),float(input(f"Enter price for {items}: "))) for i, items in enumerate(range(5))]

sorted_items_price = sorted(user, key = lambda x: x[1], reverse = True)

for items, price in sorted_items_price:
  print(f"{items}: ${price: .2f}")