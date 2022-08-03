#get a single string from two given strings and swap the first 2 characters os each string.
str1=input("Enter string number 1 : ")
str2=input("Enter string number 2 : ")
x=str1[0:2]
str1=str1.replace(str1[0:2],str2[0:2])
str2=str2.replace(str2[0:2],x)
print(str1)
print(str2)