import sys
a=(sys.argv[1])
b=len(a)
print(b)
for j in range(0,b):
	if (a[j]!=a[b-j-1]):
		 break
if j < int(b/2 + 1):
	print ("not a palindrome")
else:
	print ("palindrome")
	hsdgsagh
