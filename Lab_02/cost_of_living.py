rent = float(input("Rent per month:"))
gas = float(input("Gas payment per month:"))
electricity = float(input("Electricity payment per month:"))
water = float(input("Water payment per month:"))
tax = float(input("Council tax payment per month:"))
total = round(rent+gas+electricity+water+tax,2)

table_content = [["Rent: ", "$", rent],
                 ["Gas: ", "$", gas],
                 ["Electricity: ", "$", electricity],
                 ["Water: ", "$", water],
                 ["Council tax: ", "$", tax]]

table_format = "{:<20}{:<5}{:>3}"
print("Your monthly expenses are:")
for name,pound,money in table_content:
    print(table_format.format(name,pound,money))
print("==============================")
print(table_format.format("Total: ", "$", total))