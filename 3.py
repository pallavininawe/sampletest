import sys
a=(sys.argv[1])
b=len(a)
print(b)
for i in range(0,b):
	if (a[i]!=a[b-i-1]):
		 break
if i < int(b/2 + 1):
	print ("not a palindrome")
else:
	print ("palindrome")