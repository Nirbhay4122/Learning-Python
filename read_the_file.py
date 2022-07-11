# For open the file we use open() function
n = open("for_read_file_practice.txt")

"""
# For read the file we use read() function
print(n.read())
"""

"""
# For read line we use readline() function
print(n.readline())
print(n.readline())
print(n.readline())
"""

"""
# For read the lines as the list then we use readlines() function
print(n.readlines())
"""

"""
# For read the charactor vise paragraph we use the function read(no of charactors)
print(n.read(18))
"""

"""
# For itrate the lines we use as given below
for line in n:
    print(line)
"""

n.close()