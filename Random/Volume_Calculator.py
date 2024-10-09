# Box class
class Box:
    def __init__(self, length, width, height):
        self.__length = length  # Private attribute
        self.__width = width    # Private attribute
        self.__height = height  # Private attribute

    # Method to allow access to the dimensions (similar to a friend function)
    def get_dimensions(self):
        return self.__length, self.__width, self.__height

# Function to print dimensions of the box (simulating friend function behavior)
def print_dimensions(box):
    length, width, height = box.get_dimensions()
    print(f"Length: {length}, Width: {width}, Height: {height}")

# VolumeCalculator class
class VolumeCalculator:
    # Method to calculate and return the volume of a box
    def calculate_volume(self, box):
        length, width, height = box.get_dimensions()
        return length * width * height

# Main program
if __name__ == "__main__":
    # Create a Box object
    box = Box(3.0, 4.0, 5.0)

    # Use the function to print dimensions
    print_dimensions(box)

    # Create a VolumeCalculator object
    vc = VolumeCalculator()

    # Calculate and print the volume of the box
    volume = vc.calculate_volume(box)
    print(f"Volume of the box: {volume} cubic units")
