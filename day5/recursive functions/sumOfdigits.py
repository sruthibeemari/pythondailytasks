def sumOf_digits(n):
    if n==0:
        return 0
    else:
       return n % 10 + sumOf_digits(n//10)
print(sumOf_digits(1234))
        