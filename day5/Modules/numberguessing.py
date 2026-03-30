import random
import math
num=random.randint(1,50)
choices=5
print("Number guessing game\n " 
     "guess between 1 to 50\n " 
      "you have 5 attempts\n " 
       "let's start")
for i in range(choices):
    guess=int(input("guess the number: "))
    difference=int(math.fabs(num-guess))
    if guess==num:
        print("Congrats! you won the game ")
        break
    else:
        print("wrong guess")
        print("You are",difference,"away from the correct one")
        print("Attempts left: ",choices-(i+1))
else:
    print("you lost the  game '~' the number was: ",num)
   