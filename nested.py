inp=int(input("Enter a password : "))


if(inp < 0):
    print("number is negative")
elif(inp>0):
    if(inp<=10):
        print("number is positive and less than or equal to 10")
    elif(inp<=20):
        print("number is positive and less than or equal to 20")
    else:
        print("number is positive and greater than 20")
else:
    print('number is invalid')