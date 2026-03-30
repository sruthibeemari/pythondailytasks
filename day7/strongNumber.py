import math
num=int(input("enter a number: "))

temp=num
sum=0

while temp>0:
    digit=temp%10
    sum=sum+ math.factorial(digit)
    temp=temp//10
if sum==num:
    print("Given number is strong number")
else:
    print("not a strong number")