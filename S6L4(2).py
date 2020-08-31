from itertools import cycle
my_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]

iter = cycle(my_list)
stop = ''
while stop != 'q':
    print(next(iter), end='')
stop = input()






