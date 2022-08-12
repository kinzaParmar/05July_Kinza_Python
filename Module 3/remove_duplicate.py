#write a program to remove duplicate values from a list

list = [1, 2, 3, 4, 3, 2]

temp = []

for x in list:
    if x not in temp:
        temp.append(x)

list = temp

print(f'Updated List after removing duplicates = {temp}')   