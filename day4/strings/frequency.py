s1="hello"
freq={}
for i in s1:
    if i in freq:
        freq[i]+=1
    else:
       freq[i]=1
print(freq)