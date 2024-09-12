from lib2to3.fixer_util import String

word = input("Enter the string :")

lowerCount = 0
upperCount = 0

for i in word:
    if i.islower():
        lowerCount += 1
    else:
        upperCount += 1

print("the number of lower character is : " , lowerCount )
print("the number of upper character is : " , upperCount )