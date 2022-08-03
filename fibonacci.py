#fibonacci series
digit=int(input("Enter number for fibonacci series : "))
n1,n2=0,1
n=0
if digit<=0:
    print("Number must be bigger than 0")
else:
    for i in range(0,digit):
        print(n,end=" ")
        n1=n2
        n2=n
        n=n1+n2
