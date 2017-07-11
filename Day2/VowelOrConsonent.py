import string
a=raw_input("Enter a letter : ")
upper=a.upper()
if ( upper == 'A' or upper == 'E' or upper== 'I' or upper== 'O' or upper== 'U'):
	print("Vowel")
else:
	print("Consonent")