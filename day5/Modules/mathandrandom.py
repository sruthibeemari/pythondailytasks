import random
import math
num=[]
for i in range(20):
    number=random.randint(1,200)
    num.append(number)
print("Random numbers: ",num)

max_num=max(num)
min_num=min(num)
square_root=math.sqrt(max_num)
logrithm=math.log(min_num)
print(" maximum number: ",max_num)
print(" minimum number: ",min_num)
print("square root of maximum number: ",square_root)
print("logrithm of minimum number: ",logrithm)