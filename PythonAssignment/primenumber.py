n=int(input("enter a number : "))
pflag=0
npflag=0
primelist=[]
for i in range(2,n):
    if n%i==0:
        pflag+=1
        primelist.append(i)
    else:
        npflag+=1
if pflag>0:
    print("prime number")
else:print("not a prime number")             