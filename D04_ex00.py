#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

#body
def guess():
	x = random.randint(1, 25)
	print('number to guess: ' + str(x))

	count = 0
	value = ''
	while count < 5 and value != x:
		try:
			value = int(input('Guess what the number is:\n'))
			if value == x:
				print('Your guess is right!')
			elif value > x:
				print('Your guess is too high, please try again!')
			elif value < x:
				print('Your guess is too low, please try again!')
		except ValueError:
			print('Oops! That was no valid number. Try again...')
		count = count + 1

################################################################################
def main():


    guess() # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()