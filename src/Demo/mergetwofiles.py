with (open(r'C:\Users\hp5cd\OneDrive\Desktop\m1.txt') as f1,
      open(r'C:\Users\hp5cd\OneDrive\Desktop\m2.txt') as f2,
      open(r'C:\Users\hp5cd\OneDrive\Desktop\merge.txt' 'w') as output):
    output.write(f1.read()+f2.read())