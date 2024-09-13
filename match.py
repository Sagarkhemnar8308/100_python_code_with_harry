x = 13
match (x % 2 == 0):
    case 0:
        print(f"not Divisible by 2 {x % 2 == 0}")
    case 1:
        print(f"Divisible by 2 {x % 2 == 0}")
    case _:
        print("3", x)

