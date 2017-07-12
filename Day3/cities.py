city=(raw_input("Enter a particular city: "))
dict = {'Mumbai': 'Maharashtra', 'Noida': 'Delhi', 'Hyderabad': 'Andhra Pradesh','Kerala': 'Tamil Nadu', 'Bhopal': 'Madhya Pradesh'}
print ("Corresponding city is ", dict[city])
state=(raw_input("Enter a state: "))
print (list(dict.keys())[list(dict.values()).index(state)])
