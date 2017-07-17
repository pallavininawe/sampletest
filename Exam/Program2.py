import sys
def fun(n):
     
    # initializing value corresponding to 'A' ie. its ASCII value
   
    num = 65
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # explicitely converting to char
            charr = chr(num)
         
            # printing char value 
            print charr,
         
            # incrementing at each column
            num = num +1
     
     
        # ending line after each row
        print("\r")
 
# Driver code
n = 5
fun(n)