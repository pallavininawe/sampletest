result_str=""; 
a=int(input("Enter the number of rows"))
b=int(input("Enter the number of columns"))   
if(a>=b and b>=a/2):
	for row in range(0,a):    
	    for column in range(0,b):     
	        if ((column == 0) or (row == a-1)):    
	            result_str=result_str+"*"    
	        else:      
	            result_str=result_str+" "    
	    result_str=result_str+"\n"    
	print(result_str);
else:
	print("will not be able to print properly")