minute = int(input("Enter number of minutes:"))
charge = minute* 0.15
VAT = charge * 0.2
print("Number of minutes used:", minute)
print("Basic call charge:", charge)
print("VAT due:", VAT)
print("Total bill:", VAT+charge)