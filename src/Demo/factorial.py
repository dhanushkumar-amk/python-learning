# from math import factorial

num = int(input("Enter the value :"))
fact = 1

## base case
if num < 0:
    print("The factorial number can't be negative")
else :
    for i in range(1, num):
        fact += fact * i
print(fact)





# print(factorial(num))