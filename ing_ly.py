# Add ing at the end, if ends wit ing then add ly.
str=input("Enter a string : ")
if len(str)<3:
    print(str)
elif str[-3:] == "ing":
    print(str + "ly")
else: 
    print(str + "ing")


