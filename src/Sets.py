
#  sets acts as combination of lists and dictionary

#  all data are heterogeneous

# but all keys are unique


# it does not allow duplicates


set1 = {1,2,3,4,5,6}

print(set1)

print(type(set1))

set2 = {1,1,1,1,2,3}
print(set2)  # it doesn't allow duplication

# add element
set1.add(7)
print(set1)

# remove element
set1.remove(7)
print(set1)

# it allow's the various data type
set1.add('1')

# it does not support Boolean value
# True == 1
# false == 0

set1.add(False)

# delete all elements

# set1.clear()

print(set1)


# convert list into sets
lst = [1,2,3,4,5,6,7]
set2 = set(lst)
print(set2)


set11 = {1,2,3,4}
set22 = {5,6,7,8,4}

# union
print(set11.union(set22))

# intersection
print(set11.intersection(set22))

# difference
print(set11.difference(set22))


# traverse a set
for i in set22:
    print(i)


