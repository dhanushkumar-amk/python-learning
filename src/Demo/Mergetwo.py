# open file1 and read
file1 = open("file1.txt")
data1 = file1.read()

# # for new line
# data1 += '\n'

# open file2 and read
file2 = open("file2.txt")
data2 = file2.read()

# open file3 and  add file1 and file2 data
file3 = open("file3.txt", 'w')
file3.write(data1 + data2)

print("merge two files is successfully executed")




