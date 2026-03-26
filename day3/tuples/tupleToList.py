#tuple and list and modify
t1=(1,2,3,4,5)
x=list(t1)
x[1]=4
t1=tuple(x)
print(t1)