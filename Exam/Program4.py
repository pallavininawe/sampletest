n=int(input("Enter a number:"))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n/10
print("The total sum of digits is:",sum)