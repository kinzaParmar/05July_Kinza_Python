#find the factorial of a given number.
no=int(input("Enter a number for factorial : "))
fact=1
if no >=1:
    for i in range(1,no+1):
        fact=fact*i
        print(fact)
else:
    print("Inappropriate digit. TRY AGAIN.")

