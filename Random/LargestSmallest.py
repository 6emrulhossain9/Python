# Function to find the largest of three numbers
def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:  # Changed from else if to if for proper logic
        largest = c
    return largest

# Function to find the smallest of three numbers
def find_smallest(a, b, c):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:  # Changed from else if to if for proper logic
        smallest = c
    return smallest

# Main program
if __name__ == "__main__":
    num1, num2, num3 = map(int, input("Enter three integers: ").split())
    largest = find_largest(num1, num2, num3)
    smallest = find_smallest(num1, num2, num3)
    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")
