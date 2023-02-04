'''a=["hello","world","welcome","cs"]
b=[]
for i in range(len(a),0,-1):
    for j in range(len(a)):
        temp=a[j]
        a[j]=a[i-1]
        a[i-1]=temp
print(a)        

'''
