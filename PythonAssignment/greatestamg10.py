alist=[]
for i in range(10):
    a=int(input("enter value : "))
    alist.append(a)
print(alist)
print("length =",len(alist))  
alist.sort()
print("greatest = ",alist[-1])  
    