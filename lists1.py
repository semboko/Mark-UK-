my_list = [10, 20, 30, 40, 50]

t = my_list[2]
my_list[2] = my_list[4]
my_list[4] = t
del t

for i in range(4, -1, -1):
    print(my_list[i])