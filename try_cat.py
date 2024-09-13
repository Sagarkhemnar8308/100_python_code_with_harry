
try:
    a = int(input("Enter a num"))
    for i in range(1, 10+1):
        print(f"{a} X {i} = {a*i}")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("finally")
    
