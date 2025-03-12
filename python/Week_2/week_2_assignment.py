my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list[1] = 15
my_list.extend([50, 60, 70])
print(my_list)
del my_list[6]
print(my_list)

sorted_list = sorted(my_list)

print(sorted_list)

print(f"Index of 30: {my_list.index(30)}")