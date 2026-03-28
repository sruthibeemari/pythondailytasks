def numOf_vowels(name):
    vowels="aeiou"
    count=0
    for i in name:
        if i in vowels:
            count=count+1
    return count
print(numOf_vowels("ice cream"))
