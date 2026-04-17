import random
num=[random.randint (1,100) for i in range(10)]
print(num)
even=0
odd=0

for i in num:
    if i%2==0:
        even+=1
        
    else:
        odd+=1
print("Even: ",even)
print("Odd:",odd)

num_set=set(num)
print("Set numbers",num_set)