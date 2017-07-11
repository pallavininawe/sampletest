import sys
a=0
b=1
print(a)
print(b)
for x in range(2,50):
	c=a+b
	print(c)
	a=b
	b=c
	