Q) Define list

def printelements(elements):
    for i in elements:
        print(i,end=" ")
elements=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
        ele=int(input("Enter:"))
        elements.append(ele)
printelements(elements)
