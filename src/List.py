
# list datatype is similar to arrays python does not support arrays

#  it is used to store collection of values in an single variables


# array is a homogeneous datatype

#  list is a heterogeneous data type  => IT WILL ACCEPT MULTIPLE DATA TYPE
list = [1,2,3,4,5,6,7]

list1 = ["hi", 29, True, 34.5]

# print(list[-1])  backward indexing

l1 = [1,2,3,4]
l2 = [5,6,7,8]

#  merge the two list
l3 = l1 + l2
print(l3)

# default function
print(len(l3))  # length of list

l3.append(9)  # to add element in list
print(l3)

l4 = [10,11,12,13]
l3.extend(l4)  # to insert multiple elements in the list

print(l3)

l3.insert(1,1.5)  # to insert element in an  particular index using insert
print(l3)

print("===============")
l3.sort(reverse=True)
print(l3)


# sum
print(sum(l3))

print(l3.count(2))  # count the element in an particular list

# to identify the index of an element
print(l3.index(4))

l1.clear()  # to clear all element in an list using clear method
print(l1)

print(min(l3))
print(max(l3))

# remove an element
print(l3)
l3.pop()  # to remove an particular element default last element has been removed
print(l3)


# nested list

ll = [[1,2,3],[4,5,6]]
print(ll)

print(ll[1][2]) # accessing the particular element in nested list


# list comprehension
# use list more easily

arr = [1,2,3,4,5,6]

odd = []
even= []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

# the above lines will become one line

odd1 = [i  for i in arr if i % 2 == 1]  # but it does not efficient  to learn
print(odd1)