ini_string = "1a"
scale = 16
print ("Initial string", ini_string)
res = bin(int(ini_string, scale)).zfill(8)
print ("Resultant string", str(res))
