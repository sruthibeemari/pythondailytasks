def reverse_string(a):
    if a=="":
        return ""
    else:
        return reverse_string(a[1:])+a[0]
print(reverse_string("hello"))