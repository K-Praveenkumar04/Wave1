#intrest account earns 4 percent interest
deposit = int(input("Enter amount of money deposited: "))
interest = 0.04
year1 = (deposit * interest)
total1 = round(year1 + deposit, 2)
year2 = (total1 * interest)
total2 = round(year2 + total1, 2)
year3 = (total2 * interest)
total3 = round(year3 + total2, 2)
print ("Total in account after 1 year: " + str(total1))
print ("Total in account after 2 years: " + str(total2))
print ("Total in account after 3 years: " + str(total3))