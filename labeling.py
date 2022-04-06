# txt File Deduplication (Order Maintenance)
print('Start')

w = open('File path you want to create', 'w')
r = open('File path to be read', 'r')

# To save lines read from a file as a list
lines = r.readlines()

# To change to a list dictionary
lines = list(dict.fromkeys(lines))
print(lines)

# Writing FILE
for line in lines:
    w.write(line)

# Closing File
w.close()
r.close()

print('End')
