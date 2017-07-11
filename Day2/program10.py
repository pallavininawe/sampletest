result_str="";    
for row in range(0,8):    
    for column in range(0,6):     
        if ((column == 0) or (row == 7)):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
