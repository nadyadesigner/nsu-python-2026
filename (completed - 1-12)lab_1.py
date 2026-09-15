# Task 1 — Personal Information
# ============================================================
print("Task 1 — Personal Information")
name = input("Enter your name: ")
age = int(input('Enter your age: '))
print('Hello,', name)
print('Next year you will be', age+1, 'years old')

#=============================================================
# Task 2 — Rectangle
# ============================================================
print("Task 2 — Rectangle")
width = int(input('enter width '))
height = int(input('enter height '))
area = height*width/2
perimeter = 2*(height+width)
print("Rectanle's area is ", int(area), "Rectanle's perimeter is ", int(perimeter))

# ============================================================
# Task 3 — Temperature Converter
# ============================================================

print("Task 3 — Temperature Converter")
celsius = float(input('Enter Celsius temperature: '))
fahrenheit = 32 + celsius * 9 / 5
print('Fahrenheit temperature: ', fahrenheit)

# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")
quantity = int(input('enter quantity of items: '))
price = float(input('enter the price of one item: '))
total_price = price*quantity
discounted_price = total_price*0.9
print('Total price is ', total_price, 'discounted price is ', discounted_price)


# ============================================================
# Task 5 — Arithmetic Operators
# ============================================================

print("Task 5 — Arithmetic Operators")
a = 17
b = 5
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
print(type(integer_value), type(float_value), type(complex_value), type(text_value), type(boolean_value), sep='\n')


# ============================================================
# Task 7 — Comparisons and Boolean Logic
# ============================================================

print("Task 7 — Comparisons and Boolean Logic")
age = 22
is_master_student = True
print(age >= 18) #true
print(age < 30) #true
print(age == 22) #true
print(age != 25) #true
print(age >= 18 and is_master_student) #true
print(age < 18 or is_master_student) #true
print(not is_master_student) #false
print()


# ============================================================
# Task 8 — Python Collections
# ============================================================

print("Task 8 — Python Collections")
programming_languages = ['Python', 'Go', 'C++']
numbers = (2, 4, 5)
cities = {"New-York", "Los Angeles", "Ottawa"}
student = {'name':'Nikita', 'age':'46', 'university':'NSU'}
print(programming_languages, numbers, cities, student, sep='\n')
print(type(programming_languages), type(numbers), type(cities), type(student), sep='\n')


# ============================================================
# Task 9 — Indexing and Slicing
# ============================================================

print("Task 9 — Indexing and Slicing")
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(numbers[0])
print(numbers[-1])
print(numbers[0:4])
print(numbers[0::2])
word = "Python"
print(word[0])
print(word[-1])
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
print(student['name'])
print(student['age'])
print('"age" exists in the dictionary: ', 'age' in student)
print('"email" exists in the dictionary: ', 'email' in student)
numbers = [10, 20, 30, 40]
print('20 is in numbers: ', 20 in numbers)
print('50 is in numbers: ', 50 in numbers)
print()


# ============================================================
# Task 11 — Formatted Output
# ============================================================

print("Task 11 — Formatted Output")
radius = float(input('enter the radius of a circle: '))
area = 3.14159 * radius ** 2
print(f"Radius is: {radius:.1f}")
print(f"Area is: {area:.2f}")
print()

# ============================================================
# Task 12 — Trip Cost Calculator
# ============================================================

print("Task 12 — Trip Cost Calculator")
distance=float(input('enter distance in kilometers: '))
fuel_consumption=float(input('enter fuel consumption in liters per 100 km: '))
fuel_price=float(input('enter fuel price per liter: '))
liters_needed = (distance / 100) * fuel_consumption #36
trip_cost = liters_needed * fuel_price #2160
print(f"Distance: {distance:.2f}",
      f"Fuel required: {liters_needed:.2f}",
      f"Trip_cost: {trip_cost:.2f}", sep='\n'
)

