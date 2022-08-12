#Program to count the number of strings, where the lenght of string is 2 or more and first n last char are same 
str_list=['I','Kinza','Python','eat','is']
for i in str_list:
    str=len(i)<=2 and i[0] == i[:-1]
    str_count=str.count(i)
print(str_count)

