import random
n=random.randint(1,100)
count=5
while(count>0):
    x=int(input("Enter the number:"))
    if x<n:
        print("Too Low")
    elif x>n:
        print ("Too High")
    else:
        print("Congratulations you got the number")
        break
    count=count-1
print("You Won!")    
