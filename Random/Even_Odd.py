def even_odd(x):
    if x % 2 == 0:
        print(f"{x} is an Even Number")
    else:
        print(f"{x} is an Odd Number")

number = int(input("Enter an Integer: "))
even_odd(number)
