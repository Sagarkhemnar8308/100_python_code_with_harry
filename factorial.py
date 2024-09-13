

# a = int(input("Enter a number to fact :- "))
# fact = 1
# for i in range(1, a + 1):
#     print(i) 
#     fact = fact * i
# print(f"factorila of {a} is {fact}")


def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        print(n, n-1)
        return n * fact(n-1)

    
print(fact(5))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(f"fib({n-1}) + fib({n-2})")
        return fib(n-1) + fib(n-2)

print(fib(5))
        
