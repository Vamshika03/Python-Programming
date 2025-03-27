Q) Game
import random
n=random.randint(1,100)
while True:
    x=int(input("Enter the number:"))
    if x<n:
        print("Too Low")
    elif x>n:
        print ("Too High")
    else:
        print("Congratulations you got the number")
        break
