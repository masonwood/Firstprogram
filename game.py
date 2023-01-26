import random

random_number = random.randint(1,10)

guess = None

while guess != random_number:
	guess = input("Pick a number from 1 to 10: ").lower()
	guess = int(guess)
	if guess < random_number:
		print("Too low!")
	elif guess > random_number:
		print("Too high!")
	else:
		print("You won!")

print(random_number)