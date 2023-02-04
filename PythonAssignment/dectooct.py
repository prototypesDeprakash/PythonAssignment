# Decimal to Octal
n = int(input("Ent the no:"))
num = n
ans = ''
while num > 0:
    ans = ans+str(num % 8)
    num = num//8
print(ans[::-1])
