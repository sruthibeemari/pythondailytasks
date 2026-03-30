def Fibonacci_number(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci_number(n-1)+Fibonacci_number(n-2)
n=6
print(Fibonacci_number(n))
