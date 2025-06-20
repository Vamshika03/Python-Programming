d={}
a={}
size=2
for i in range(size):
    key=int(input("enter the key:"))
    value=input("enter the value:")
    d[key]=value
    a[value]=key
print(d)
print(a)
