data=raw_input("enter the data to append")
fname = raw_input("Enter file to be appended to: ")
with open(fname, "a") as myfile:
    myfile.write(' '+data)