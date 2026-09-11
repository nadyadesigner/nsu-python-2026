# Task 1 — Personal Information
# ============================================================
print("Task 1 — Personal Information")

# TODO:
# Ask the user to enter their name.
name = input("Enter your name: ")

# TODO:
# Ask the user to enter their age.
# Remember that input() returns a string.
age = int(input('Enter your age: '))


# TODO:
print('Hello,', name)
# Print:
# Hello, <name>!
# Next year you will be <age + 1> years old.
print('Next year you will be', age+1, 'years old')

#=============================================================
# Task 2 — Rectangle
# ============================================================
print("Task 2 — Rectangle")

# TODO:
# Ask the user to enter width and height.
width = int(input('enter width '))
height = int(input('enter height '))

# TODO:
# Calculate the area.
area = height*width/2

# TODO:
# Calculate the perimeter.
perimeter = 2*(height+width)

# TODO:
# Print the results.
print("Rectanle's area is ", int(area), "Rectanle's perimeter is ", int(perimeter))
# ============================================================
# Task 3 — Temperature Converter
# ============================================================

print("Task 3 — Temperature Converter")

# Formula:
# Fahrenheit = Celsius * 9 / 5 + 32

# TODO:
# Read Celsius temperature.

celsius = float(input('Enter Celsius temperature: '))

# TODO:
# Calculate Fahrenheit temperature.

fahrenheit = 32 + celsius * 9 / 5

# TODO:
# Print the result.

print('Fahrenheit temperature: ', fahrenheit)


# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")

# TODO:
# Ask for the number of items.

quantity = int(input('enter quantity of items: '))

# TODO:
# Ask for the price of one item.

price = float(input('enter the price of one item: '))

# TODO:
# Calculate the total price.

total_price = price*quantity

# TODO:
# Apply a 10% discount.

discounted_price = total_price*0.9

# TODO:
# Print both results.


print('Total price is ', total_price, 'discounted price is ', discounted_price)


# ============================================================
# Task 5 — Arithmetic Operators
# ============================================================

print("Task 5 — Arithmetic Operators")

a = 17
b = 5

# TODO:
# Print the result of each operation:
#
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b, sep='\n')

# ============================================================
# Task 6 — Data Types
# ============================================================

print("Task 6 — Data Types")

integer_value = 42
float_value = 3.14
complex_value = 2 + 3j
text_value = "Python"
boolean_value = True

# TODO:
# Use type() to print the type of every variable above.
#
# Example:
print(type(integer_value), type(float_value), type(complex_value), type(text_value), type(boolean_value), sep='\n')


# ============================================================
# Task 7 — Comparisons and Boolean Logic
# ============================================================

print("Task 7 — Comparisons and Boolean Logic")

age = 22
is_master_student = True

# TODO:
# Print the result of the following expressions:
#
print(age >= 18) #true
print(age < 30) #true
print(age == 22) #true
print(age != 25) #true

print(age >= 18 and is_master_student) #true
print(age < 18 or is_master_student) #true
print(not is_master_student) #false
#
# Predict each result before running the program.


print()


# ============================================================
# Task 8 — Python Collections
# ============================================================

print("Task 8 — Python Collections")

# TODO:
# Create:
#
# 1. A list containing three programming languages.
# 2. A tuple containing three numbers.
# 3. A set containing several city names.
# 4. A dictionary describing a student with:
#       name
#       age
#       university

programming_languages = ['Python', 'Go', 'C++']
numbers = (2, 4, 5)
cities = {"New-York", "Los Angeles", "Ottawa"}
student = {'name':'Nikita', 'age':'46', 'university':'NSU'}

# TODO:
# Print all four variables.

print(programming_languages, numbers, cities, student, sep='\n')

# TODO:
# Use type() to print the type of each collection.


print(type(programming_languages), type(numbers), type(cities), type(student), sep='\n')


# ============================================================
# Task 9 — Indexing and Slicing
# ============================================================

print("Task 9 — Indexing and Slicing")

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

# TODO:
# Print the first element.
print(numbers[0])

# TODO:
# Print the last element.
print(numbers[-1])

# TODO:
# Print elements from index 1 up to index 4.
print(numbers[0:4])

# Expected:
# [1, 2, 3]

# TODO:
# Print every second element.
#
print(numbers[0::2])
# Expected:
# [0, 2, 4, 6]


word = "Python"

# TODO:
# Print the first character.
print(word[0])

# TODO:
# Print the last character.
print(word[-1])

# TODO:
# Print:
# Pyt
print(word[0:3])


# ============================================================
# Task 10 — Dictionaries and Membership
# ============================================================

print("Task 10 — Dictionaries and Membership")

student = {
    "name": "Anna",
    "age": 22,
    "city": "Novosibirsk",
}

# TODO:
# Print the student's name.
print(student['name'])


# TODO:
# Print the student's age.
print(student['age'])

# TODO:
# Check whether "age" exists in the dictionary.
# Print the result.
print('"age" exists in the dictionary: ', 'age' in student)

# TODO:
# Check whether "email" exists in the dictionary.
# Print the result.
print('"email" exists in the dictionary: ', 'email' in student)


numbers = [10, 20, 30, 40]

# TODO:
# Check whether 20 is in numbers.
print('20 is in numbers: ', 20 in numbers)

# TODO:
# Check whether 50 is in numbers.
print('50 is in numbers: ', 50 in numbers)

print()


# ============================================================
# Task 11 — Formatted Output
# ============================================================

print("Task 11 — Formatted Output")

# TODO:
# Ask the user to enter the radius of a circle.

radius = float(input('enter the radius of a circle: '))

# Use:
# area = 3.14159 * radius ** 2

area = 3.14159 * radius ** 2

# TODO:
# Print the radius and area using an f-string.
#
# Example:
# Radius: 10.0
# Area: 314.16
#
# Print the area with exactly two digits after the decimal point.
#
# Hint:
# {value:.2f}


print(f"Radius is: {radius:.1f}")
print(f"Area is: {area:.2f}")
print()

# ============================================================
# Task 12 — Trip Cost Calculator
# ============================================================

print("Task 12 — Trip Cost Calculator")

# A car consumes a certain number of liters of fuel
# for every 100 kilometers.

# TODO:
# Ask the user to enter:
#
# distance in kilometers #450
distance=float(input('enter distance in kilometers: '))
# fuel consumption in liters per 100 km #8
fuel_consumption=float(input('enter fuel consumption in liters per 100 km: '))
# fuel price per liter #60
fuel_price=float(input('enter fuel price per liter: '))

# TODO:
# Calculate how many liters of fuel are required.
#
# Formula:
liters_needed = (distance / 100) * fuel_consumption #36

# TODO:
# Calculate the total cost of the trip.

trip_cost = liters_needed * fuel_price #2160

# TODO:
# Print something similar to:
#
# Distance: 450.0 km
# Fuel required: 36.00 liters
# Trip cost: 2160.00
#
# Use f-strings and two decimal places where appropriate.
print(f"Distance: {distance:.2f}",
      f"Fuel required: {liters_needed:.2f}",
      f"Trip_cost: {trip_cost:.2f}", sep='\n'
)

