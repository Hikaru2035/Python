#Input data(W, L & H)
width = int(input("Please enter width: "))
length = int(input("Please enter length: "))
height = int(input("Please enter height: "))

#Calculation
cuboid = width*length*height
surface = (2*width*height)+(2*width*length)+(2*length*height)

#Output
print("Surface area should be", surface)
print("Volume should be ", cuboid)
