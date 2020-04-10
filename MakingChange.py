#making change
cents = int(input("Enter amount of cents: "))
toonie = 200
loonie = 100
quarter = 25
dime = 10
nickle = 5
print ("Amount of change returned: ")
print(str(cents // toonie) + " toonie(s)")
cents = cents % toonie
print(str(cents // loonie) + " loonie(s)")
cents = cents % loonie
print(str(cents // quarter) + " quarter(s)")
cents = cents % quarter
print(str(cents // dime) + " dime(s)")
cents = cents % dime
print(str(cents // nickle) + " nickle(s)")
cents = cents % nickle
print (str(cents) + " pennie(s)")