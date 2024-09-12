from statistics import median

list1 = [12,16,20,12,30,25,23,24,20]

# mean
sum = 0
for i in list1:
    sum += i
mean = sum // len(list1)
print(mean)

# median

list1.sort()
if len(list1) % 2 == 0:
    m1 = list1[len(list1) // 2]
    m2 = list1[len(list1)// 2 - 1]
    median = ( m1 + m2 )/ 2
else:
    median = list1[len(list1) // 2]
print(median)


#  mean

frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())

mode = [i for i, j in frequency.items() if j == frequent]
print(mode)