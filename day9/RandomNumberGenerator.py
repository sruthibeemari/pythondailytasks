def randomGen(n):
    for i  in range(1,n+1):
        yield i
    
n=int(input("enter n value: "))
gen=randomGen(n)

for num in gen:
    print(num)