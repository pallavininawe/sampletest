result_str=""; 
a=int(input("Enter the number of rows"))
b=int(input("Enter the number of columns"))   
if(b%2!=0 and a>=b and b>=a/2 and b>3):
	for row in range(0,a):    
	    for column in range(0,b):     
	        if ((column == 0) or (column == b-1) or (row == a/2 and column== b/2) or ((row == a/2-1)and (column ==b/2-1)) or ((row == a/2-1)and (column ==b/2+1))):  
	            result_str=result_str+"*"    
	        else:      
	            result_str=result_str+" "    
	    result_str=result_str+"\n"    
	print(result_str);
else:
	print("will not be able to print properly")