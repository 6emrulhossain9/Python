# Function to check if a number is a palindrome
def is_palindrome(number):
    original_number = number
    reversed_number = 0

    # Reverse the number
    while number != 0:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder
        number //= 10

    # Check if the original number and reversed number are the same
    return original_number == reversed_number

# Input a number
num = int(input("Enter a number: "))

# Call the function
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
