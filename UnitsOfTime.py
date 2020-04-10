#time
days = int(input("Enter number of day(s): "))
hours = int(input("Enter number of hour(s): "))
minutes = int(input("Enter number of minute(s): "))
seconds = int(input("Enter number of second(s): "))
secsinday = 86400
secsinhour = 3600
secsinminute = 60
totalday = days * secsinday
totalhour = hours * secsinhour
totalminute = minutes * secsinminute
totalsecond = seconds
print ("Total number of seconds: " + str(totalday + totalhour + totalminute + totalsecond))