import sys
def calculate():
	operation = raw_input('''
	Please type in the math operation you would like to complete:
	+ for addition
	- for subtraction
	* for multiplication
	/ for division
	% for mod
	''')

	number_1 = (raw_input('Please enter the first number: '))
	number_2 = (raw_input('Please enter the second number: '))
    
	#if((isinstance(number_1,int)==True) and (isinstance(number_2,int)==True)):
	if ((number_1.isdigit()==True) and ((number_2.isdigit())==True)):
	
		if operation == '+':
			number_1 = int(number_1)
			number_2 = int(number_2)
			print('{} + {} = '.format(number_1, number_2))
			print(number_1 + number_2)

		elif operation == '-':
			number_1 = int(number_1)
			number_2 = int(number_2)

			print('{} - {} = '.format(number_1, number_2))
			print(number_1 - number_2)

		elif operation == '/':
			number_1 = int(number_1)
			number_2 = int(number_2)

			if(number_2!=0):
				print('{} / {} = '.format(number_1, number_2))
				print(number_1 / number_2)
			else:
				print("error: zero divisor. Please enter non zero value for the divisor")

		elif operation == '*':
			number_1 = int(number_1)
			number_2 = int(number_2)

			print('{} * {} = '.format(number_1, number_2))
			print(number_1 * number_2)

		elif operation == '%':
			number_1 = int(number_1)
			number_2 = int(number_2)

			print('{} % {} = '.format(number_1, number_2))
			print(number_1 % number_2)
		
		else:
			print('You have not typed a valid operator, please run the program again.')
			again()
		# Add again() function to calculate() function
		
		again()
	else:
		print("Enter Interger values")
		again()

def again():
	calc_again = raw_input('''
	Do you want to calculate again?
	Please type Y for YES or N for NO.
	''')

	if calc_again.upper() == 'Y':
		calculate()
	elif calc_again.upper() == 'N':
		print('See you later.')
	else:
		again()

calculate()