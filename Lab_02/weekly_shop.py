def shopping_list(category):
    print(category)
    sum = 0
    total = 0
    quantity = int(input("How many?"))
    price = float(input("Price?"))
    sum += quantity
    total += (quantity*price)
    return sum, total

shopping_list("Peaches")
shopping_list("Beans")
shopping_list("Chicken pieces")
shopping_list("Socks")
shopping_list("Bottle of water")
