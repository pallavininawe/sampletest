import sys
a=raw_input("Type C for Converting Celsius or Type F for Converting Fahrenheit : ")
print (a)
if a=='C':
	degree=int(input("Enter the temperature : "))
	result = int(round((9 * degree) / 5 + 32))

 	o_convention = "Fahrenheit"

elif a=='F':
	degree=int(input("Enter the temperature : "))
	result = int(round((degree - 32) * 5 / 9))

	o_convention = "Celsius"

else:

 	print("Input proper convention.")

	quit()

print("The temperature in", o_convention, "is", result, "degrees.")