a=open("file.txt","w")
a.write("qwertyuiopasdfghjklzxcvbnm")
a.write("\ngoodmorning belugua")
a.write("\nsfvbjksfvbjkfvbjksfbkj")
a=open("file.txt","r")
a.seek(29)
print(a.tell())
print(a.read())