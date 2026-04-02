def evenGenerator():
    num=2
    while True:
        yield num
        num+=2

n=int(input("Enter how many even numbers: "))
count=0
for i in evenGenerator():
    if count==n:
        break
    print(i)
    count+=1
