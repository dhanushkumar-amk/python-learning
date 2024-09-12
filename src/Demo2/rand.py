import random

num = int(input("enter the number :"))

list = []

for i in range(num):
    list.append(random.randint(1,8))
print(list)