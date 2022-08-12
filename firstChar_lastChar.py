#program to get a string made up of first two and last two charcs of a string 

str=input("Enter a string : ")
if len(str)>2:
    a=str[0:2] + str[-2:]
    print(a)
else:
    print(str)