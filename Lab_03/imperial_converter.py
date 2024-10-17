feet = int(input("Feet:"))
inches = int(input("Inches:"))

def calculation(feet,inches):
    meters = (feet*0.3048) + (inches *0.0254)
    km = meters/100
    cm = meters*100
    mm = cm*10
    print("Kilometers:",km)
    print("Meters:",meters)
    print("Centimeters:",cm)
    print("Milimeters:",mm)

calculation(feet,inches)