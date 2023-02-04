def dectobin(decimal):
    if(decimal > 0):
        dectobin((int)(decimal/2))
        print(decimal%2, end='')
        
decimal = int(input("Enter a decimal number \n"))
dectobin(decimal)