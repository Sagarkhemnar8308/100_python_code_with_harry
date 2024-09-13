# def gmean(x,y):
#     return (x*y)/(x/y)


# a=gmean(12,3)
# b=gmean(4,56)
# print(a ,b)


def avg(*num):
    print(type(num))
    total_sum = 0
    for i in num:
        total_sum += i
    return total_sum / len(num)

a=avg(1,2,3,4,5)
print(a)

def num(**num):
    print(type(num))
    print(num)
    


num(a="samir",b="amit",c="star")
