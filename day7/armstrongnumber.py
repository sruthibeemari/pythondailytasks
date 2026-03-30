number=int(input("enter a number: "))

temp=number
sum=0
while temp>0:
    digit=temp % 10
    sum=sum + digit**3
    temp=temp // 10

if sum==number:
    print("Given number is Armstrong number")
else:
    print("not an armstrong number")
