# Main program
if __name__ == "__main__":
    binary = input("Enter a binary number: ")
    decimal = 0

    # Iterate over each bit in the binary string
    for i in range(len(binary)):
        # Convert the character '0' or '1' to its numeric value (0 or 1)
        bit = int(binary[i])

        # Calculate the power of 2 for the current position
        power = len(binary) - 1 - i

        # Add the corresponding value to the decimal number
        decimal += bit * (1 << power)  # Using bit shifting for powers of 2

    print(f"Decimal: {decimal}")
