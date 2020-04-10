duration = int(input("Enter number of seconds: "))
day = 86400
hour = 3600
minute = 60
totaldays = duration // day
duration = duration % day
totalhours = duration // hour
duration = duration % hour
totalminutes = duration // minute
duration = duration % minute
totalseconds = duration
print ("D:HH:MM:SS")
print (str(totaldays).zfill(2) + ":" + str(totalhours).zfill(2) + ":" + str(totalminutes).zfill(2) + ":" + str(totalseconds).zfill(2))