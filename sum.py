#Sum of 3 integers, if values of 2 integers are same then return zero
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number : "))
sum=num1+num2+num3
if num1==num2 or num2==num3 or num1==num3:
    print("zero")
else:
    print(sum)

