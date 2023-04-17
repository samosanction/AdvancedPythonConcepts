# Creating a dictionary from a list
my_dict = {num: num * 2 for num in [1, 2, 3]}
print(my_dict)

# Picking out the letters that appears more than once


some_list = ['a', 'b', 'd', 'c', 'd', 'n', 'm', 'n', 'f']

# Long Version
new_list = []
for item in some_list:
    if some_list.count(item) > 1:
        new_list.append(item)

print(list(set(new_list)))

# Short version using COMPREHENSION

print(list(set(x for x in some_list if some_list.count(x) > 1)))

