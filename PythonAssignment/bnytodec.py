# Binary to Decimal
bn = int(input("Ent the no in binary format:"))
n = bn  # 1111
i = len(str(bn))-1
dg = 0
sum = 0
while n != 0:
    dg = n % 10
    n = n//10
    dg = dg*(2**i)
    sum += dg
    i -= 1
print(sum)
