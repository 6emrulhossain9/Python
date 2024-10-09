# Main program
if __name__ == "__main__":
    base = float(input("Enter the base: "))
    power = int(input("Enter the power: "))
    result = 1.0

    while power != 0:
        result *= base
        power -= 1

    print(f"Result: {result}")
