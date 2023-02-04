num=int(input("enter a number : "))
tempno2=num
amst=0
tempno=0
while num!=0:
    tempno=num
    tempno=tempno%10
  
    amst=amst+tempno**3
    num=num//10
print(amst)  

if tempno2==amst:
    print("the entered number is a amstrong number")
else:print("not a amstrong number ")    
