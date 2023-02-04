n=int(input("enter a number : "))
rev=0
tempn=0
while n!=0:
    tempn=n
    tempn=tempn%10
    rev=rev*10+tempn
    n//=10
print(rev)    