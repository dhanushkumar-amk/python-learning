num = int(input("enter the number :"))

fact = 1
for i in range(2, num+1):
    fact = fact * i
print(f"the factorial {num} is : ", fact)