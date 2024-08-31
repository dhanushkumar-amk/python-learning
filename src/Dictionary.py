from tabnanny import process_tokens

#  dictionary is called in java is a hashmap
# it store key and value pairs
# every key is unique

map = {
       1 :'one',
       2 :'two',
       3 :'three',
       4 :'four'
    }

print(map)

#  every key has unique value can't be assign another value

#  key must be a immutable value
# value can be anything

# access the element
print(map[1])  # only access by using key not index
print(map[2])

# functions

# access the value
print(map.get(1))  # alternative for map[1]

# length
print(len(map))

# get all the key only
print(map.keys())

# get only values
print(map.values())

# items  => it is used to convert into list
print(map.items())

# insert an new element

map[5] = 'five'

# pop
map.pop(5) # remove an las element it accepts the key value

print(map)

