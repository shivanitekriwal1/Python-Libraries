import random
print("Enter a number between 1 and 100")
random_number = random.randint(1,100)
found = False
while not found:
    number = int(input("Your Guess"))
	if number== random_number:
            print "Right Answer"
            found =True
        elif random_number<number:
	    print "Guess Lower"
	elif random_number<number:
	    print "Guess Higher"


