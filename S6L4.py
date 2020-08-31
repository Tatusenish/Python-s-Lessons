from itertools import count
from sys import argv
i = int(argv)
for i in count(i):
    if i > 10:
        exit()
    else:
        print(i)


