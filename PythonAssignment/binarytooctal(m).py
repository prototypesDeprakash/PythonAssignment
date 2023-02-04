a=int(input("enter a binary number: "))
alist=[]

octs={0:0,1:1,10:2,11:3,100:4,101:5,110:6,111:7}


if len(str(a))<=3:
    print(octs[a])
if len(str(a))>3:
    while a!= 0:
        temp=a%1000
        alist.append((octs[temp]))
        a=a//1000   
    alist.reverse()
    print(alist)
    