n=int(input("enter a number : "))
rev=0
temp=0
while n!=0:
    temp=n
    temp = temp%10
    rev=rev*10+temp
    n//=10
print(rev)    
if n==rev:
    print("pallindrom")
else:print("not a pallindrom")    