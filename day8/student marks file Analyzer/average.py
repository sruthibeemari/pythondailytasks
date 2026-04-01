total=0
count=0

file=open("marks.txt","r")
for line in file:
    name,marks=line.split()
    total+=int(marks)
    count+=1

file.close()

print("Average =",total/count)
