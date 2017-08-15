import calendar
yy=int(input("Enter  a 4 digit year"))
mm= int(input("Enter a 2 digit month"))
dd= int(input("Enter a 2 digit day"))

print(calendar.month(yy,mm))

if calendar.weekday(yy,mm,dd)==0:
	print "Monday"
elif calendar.weekday(yy,mm,dd)==1:
	print "Tuesday"
elif calendar.weekday(yy,mm,dd)==2:
	print "Wednesday"
elif calendar.weekday(yy,mm,dd)==3:
	print "Thursday"
elif calendar.weekday(yy,mm,dd)==4:
	print "Friday"
elif calendar.weekday(yy,mm,dd)==5:
	print "Saturday"
elif calendar.weekday(yy,mm,dd)==6:
	print "Sunday"

