num=int(input('enter a number : '))
temp=0
sum=0
while num!=0:
    temp=num
    temp=temp%10
    sum+=temp
    num=num//10
print(sum)    
    