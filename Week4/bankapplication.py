Q)Bank Application:




def credit(balance,transactions,amount):
    balance+=amount
    transactions.append(amount)
    print(amount,"Sucess")
    return balance,transactions
    
    
def debit(balance,transactions,amount):
    if balance<amount:
        print("Insufficient Balance")
    else:
        balance-=amount
        transactions.append(-amount)
    return balance,transactions
    
def showbalance(balance):
    print("Balance=",balance)
    
def lastfivetranscations(transaction):
    print("Transaction are:",transaction)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
balance=0
transaction=[]

while (True):
    print("Credit")
    print("Debit")
    print("Current Balance")
    print("Last five transactions")
    choice=int(input("Enter your choice:"))
    if choice==1:
        amount=int(input("Enter the amount:"))
        balance,transactions=credit(balance,transaction,amount)
    elif choice==2:
        amount=int(input("Enter the amount:"))
        balance,transactions=debit(balance,transaction,amount)
    elif choice==3:
        showbalance(balance)
    else:
        lastfivetranscations(transactions)

    
    
    
