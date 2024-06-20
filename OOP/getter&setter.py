class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self._radius = new_radius
        else:
            print("Radius must be a positive value.")

# Creating an instance of the Circle class
my_circle = Circle(5)

# Using the property to retrieve the radius
print(my_circle.radius)  # Output: 5

# Using the property to set a new radius
my_circle.radius = 8

# Retrieving the updated radius using the property
print(my_circle.radius)  # Output: 8

# Trying to set a negative radius
my_circle.radius = -3  # Output: Radius must be a positive value.

# Radius remains unchanged
print(my_circle.radius)  # Output: 8

