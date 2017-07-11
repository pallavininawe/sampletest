import string
b=raw_input("Enter a letter : ")
upper=b.upper()
if ( upper == 'A' or upper == 'E' or upper== 'I' or upper== 'O' or upper== 'U'):
	print("Vowel")
else:
	print("Consonent")