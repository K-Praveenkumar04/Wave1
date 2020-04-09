# volume of a cylinder is v = pi r*r*h
radius = int(input("Enter the radius: "))
height = int(input("Enter the heignt: "))
pi = 3.14159265
volume = round(pi * radius * radius * height, 1)
print ("Volume of the cylinder: " + str(volume))