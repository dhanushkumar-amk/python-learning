

word = input("Enter the word : ")

lowerCount = 0
upperCount = 0

for i in word:
    if i.islower():
        lowerCount += 1
    else:
        upperCount += 1

print("The lower count = ", lowerCount)
print("The upper count = ", upperCount)