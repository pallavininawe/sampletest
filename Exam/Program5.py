def missing_numbers(num_list):
      #print(num_list[0], num_list[-1] + 1)
      original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
      #print original_list
      #print num_list
      num_list = set(num_list)
      #print num_list
      return (list(num_list ^ set(original_list)))
a=input("Enter a sorted list: ")
print(missing_numbers(a))
