def is_Power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0
a=input("enter a number to check whether its a power of two: ")
print(is_Power_of_two(a))
