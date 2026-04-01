lines=0
words=0
characters=0
file=open("article.txt","r")
for line in file:
    lines+=1
    characters+=len(line)
    words+=len(line.split())
file.close()

print("number of lines: ",lines)
print("number of words: ",words)
print("number of characters: ",characters)