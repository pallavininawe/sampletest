result_str="";    
for row in range(0,7):    
    for column in range(0,5):     
        if (((column == 0)) or ((row == 0 or row == 6)) or ((row == 3) and column != 4)):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
