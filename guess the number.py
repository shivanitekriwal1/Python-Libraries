import random
number = int(input("Enter a number between 1 and 100"))
num = random.randint(1,100)
while number!=num:
	if num<n:
		print "Guess Higher"
	elif num>n:
		print "Guess Lower"

if number ==num:
	print "You Got It"


