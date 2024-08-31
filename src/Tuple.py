
# it act as a list but only difference id mutability

# tuple is a immutable => can't be change

tup = (1,2,3,4,5,6,7,7)
print(tup)

# accessing the element in tuple using index value
print(tup[0])

# len
print(len(tup))

# max
print(max(tup))

# min
print(min(tup))

#count
print(tup.count(7))

#index
print(tup.index(6))

# convert tuple into list

lst4 = list(tup)
print(lst4)

#  convert list into tuple

lst5 = tuple(lst4)
print(lst5)


