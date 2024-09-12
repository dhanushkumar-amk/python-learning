import random

num = int(input("Enter the range : "))
list = []

for i in range(num):
    list.append(random.randint(1,10))

print(list)
