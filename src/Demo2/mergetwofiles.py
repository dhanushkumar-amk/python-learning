
file1 = open('C:\\Users\\hp5cd\\Documents\\python-Learning\\pythonProject\\src\\file1.txt')
data1 = file1.read()

data1 += '\t'

file2 = open('C:\\Users\\hp5cd\\Documents\\python-Learning\\pythonProject\\src\\file2.txt')
data2 = file2.read()

file3 = open("C:\\Users\\hp5cd\\Documents\\python-Learning\\pythonProject\\src\\file3.txt", 'w')
file3.write(data1 + data2)