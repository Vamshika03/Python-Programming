Q)Fibonacci series:

a=0
b=1
count=int(input("Enter the number of terms:"))
while(count>0):
    print(a, end=" ")
    a,b=b,a+b
    count=count-1
