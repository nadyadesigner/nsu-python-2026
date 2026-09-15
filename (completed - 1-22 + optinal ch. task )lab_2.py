# ============================================================
# Task 1 — Built-in Functions
# ============================================================

print("Task 1 — Built-in Functions")

values = [12, 7, 19, 5, 14]

# TODO:
# Using built-in functions, calculate and print:
#
# number of values
print(len(values))
# smallest value
print(min(values))
# largest value
print(max(values))
# total
print(sum(values))
# mean
print(sum(values)/len(values))

#
# Do not calculate these manually.


# TODO:
# Print the results using f-strings.


print()


# ============================================================
# Task 2 — Absolute Value and Rounding
# ============================================================

print("Task 2 — Absolute Value and Rounding")

temperature_change = -7.438
measurement = 19.87654

# TODO:
# Print the absolute value of temperature_change.
print(abs(temperature_change))
# Expected numerical value:
# 7.438

# TODO:
# Round measurement to:
#
# 1 decimal place
print(round(temperature_change, 1))
# 2 decimal places
print(round(temperature_change, 2))
# 3 decimal places
print(round(temperature_change, 3))
#
# Use round().


print()


# ============================================================
# Task 3 — Assignment and Augmented Assignment
# ============================================================

print("Task 3 — Assignment and Augmented Assignment")

balance = 1000.0

# Perform the following operations using augmented assignment:
#
# 1. Add 250 to the balance.
balance += 250
print(balance)
# 2. Subtract 120.
balance -= 120
print(balance)
# 3. Multiply the remaining balance by 1.05.
balance *= 1.05
print(balance)
# TODO:
# Replace the normal assignments below with +=, -=, and *=.

balance += 250
balance -= 120
balance *= 1.05

# TODO:
# Print the final balance with two decimal places.
print('The final balance with two decimal places: ', round(balance, 2))

print()

# ============================================================
# Task 4 — Operator Precedence
# ============================================================

print("Task 4 — Operator Precedence")

# Before running the program, predict each result.

expression_1 = 2 + 3 * 4 #14
expression_2 = (2 + 3) * 4 #20
expression_3 = 20 / 5 + 3 #7
expression_4 = 20 / (5 + 3) #20/8 = 2,5
expression_5 = 2 ** 3 ** 2 #64 is uncorrect, correct is 512!

# TODO:
# Print each expression and its result.
#
print(expression_1, expression_2, expression_3, expression_4, expression_5)
# Example:
# 2 + 3 * 4 = 14


print(expression_1+expression_2+expression_3+expression_4+expression_5)


# ============================================================
# Task 5 — Time Conversion
# ============================================================

print("Task 5 — Time Conversion")

# TODO:
# Ask the user to enter a number of seconds.

total_seconds = int(input('enter a number of seconds: '))

# TODO:
# Convert the input to int.


# TODO:
# Calculate:
#

minutes=total_seconds//60
remaining_seconds=total_seconds-minutes*60

# whole minutes
# remaining seconds
#
# Example:
# 135 seconds -> 2 minutes and 15 seconds
#
# Hint:
# // and %

print(minutes, 'minute(s)', 'and', remaining_seconds, 'second(s)')

# TODO:
# Print:
# 135 seconds = 2 minute(s) and 15 second(s)


print()

# ============================================================
# Task 6 — Conversion Is Not Always Reversible
# ============================================================

print("Task 6 — Type Conversion")

value = 17.95

# TODO:
# Convert value to int and print it.

print(int(value))

# Question:
# Does int() round the value? - no, int() shows only integer part

integer_value = int(value)

# TODO:
# Convert integer_value back to float and print it.

float_value = float(value)
print(float_value)

# TODO:
# Convert integer_value to str and print:
str_value=str(value)
print(str_value, str_value[3], sep='\n')
print(type(str(value)))


# ============================================================
# Task 7 — Basic String Operations
# ============================================================

print("Task 7 — Basic String Operations")

first_name = input("First name: ")
last_name = input("Last name: ")

# TODO:
# Create full_name using string concatenation.

full_name = first_name + ' ' + last_name + ' '

# TODO:
# Print:
#
# Full name: <full_name>
# Number of characters: <length>
# First character: <first character>
# Last character: <last character>
# First three characters: <slice>

print(full_name)
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(full_name[0:3])

# TODO:
# Print full_name three times using string repetition.
full_name3=full_name * 3
print(full_name3)
# ============================================================
# Task 8 — Useful print() Options
# ============================================================

print("Task 8 — Useful print() Options")

language = "Python"
course = "AI and Big Data Analytics"
university = "NSU"

# TODO:
# Print the three values on one line separated by:
#
#  |
#
print(language, course, university, sep=' | ')

# Expected:
# Python | AI and Big Data Analytics | NSU
#
# Use sep=


# TODO:
# Use two print() calls and end= so that the result is:
#
# Python Programming
#
# Do not write "Python Programming" as one string.


print(language, end=' ')
print('Programming')



# ============================================================
# Task 9 — Collections and Choosing Data Structures
# ============================================================

print("Task 9 — Collections")

student_name = "Anna"
student_age = 22
student_skills = ["Python", "Mathematics", "Machine Learning"]
student_university = "NSU"

# TODO:
# Create a dictionary named student with the keys:
#
# name
# age
# skills
# university

student = {'name': 'Anna', 'age': 22, 'skills': ["Python", "Math", "English"], 'university': 'NSU'}

# TODO:
# Print:
#
# student's name
print(student['name'])
# student's university
print(student['university'])
# first skill
print(student['skills'][0], student['skills'][1], sep='\n')
# number of skills
print(len(student['skills']))
# Use dictionary access, indexing, and len().


 ============================================================
# Task 10 — Mutable and Immutable Objects
# ============================================================

print("Task 10 — Mutable and Immutable Objects")

# List example — mutable

numbers = [10, 20, 30]
same_numbers = numbers

# TODO:
# Change the first item in numbers to 99.

numbers.insert(0, 99)
print(numbers, same_numbers)
# numbers
# same_numbers
#
# Observe what happened.


# String example — immutable

text = "Python"
same_text = text

# TODO:
# Create a new string by adding " Course" to text.

new_text=text+' '+"Course"
print(text, same_text, new_text, sep='\n')
# Then print:
#
# text
# same_text
#
# Compare this result with the list example.


print()


# ============================================================
# Task 11 — Small Statistics Report
# ============================================================

print("Task 11 — Small Statistics Report")

scores = [78, 92, 85, 69, 88]

# TODO:
# Calculate:
#
# number of scores
number = len(scores)
# minimum score
min_scores = min(scores)
# maximum score
max_scores = max(scores)
# total score
sum_scores = sum(scores)
# mean score
mean_score=sum(scores)/len(scores)
#
# Use built-in functions.


# TODO:
# Print a clean report:
#
# Number of scores: 5
# Minimum: 69
# Maximum: 92
# Mean: 82.40
#
# Format the mean to exactly two decimal places.


print(f" Number of scores: {number}\n",
    f"Minimum: {min_scores}\n",
    f"Maximum: {max_scores}\n",
    f"Mean: {mean_score}\n")



# ============================================================
# Task 12 — PEP 8 Cleanup
# ============================================================

print("Task 12 — PEP 8 Cleanup")

# The following code works, but it is difficult to read.
#
# TODO:
# Rewrite it using:
#
# meaningful variable names
# snake_case
# spaces around operators
# intermediate variables
# formatted output
#
# Keep the same calculation.

Price = 1250
Quantity = 3
Discount_percent = 10
Total_price = Price * Quantity - Discount_percent / 100 * Price * Quantity

print("Final price is: ",Total_price)

# ============================================================
# Optional Challenge — Student Score Summary
# ============================================================

print("Optional Challenge — Student Score Summary")

# Create a small program using only concepts from Sections 1–2.
#
# Ask the user for:
#
# student name
# three test scores
#
name=input('enter your name: ')

score_1, score_2, score_3 = float(input('enter a first score ')), float(input('enter a second score ')), float(input('enter a third score '))
# Store the three scores in a list.

scores=[score_1, score_2, score_3]
# Calculate:

min_score=min(scores)
# minimum score
max_score=max(scores)
# maximum score
mean_score=sum(scores)/len(scores)
# mean score
#
# Print a clean summary similar to:
#
print(f"Student: {name}",
      f"Scores: {scores}", f"Minimum: {min_score}", f"Maximum: {max_score}",
      f"Mean: {mean_score:.2f}", sep='\n')

# Student: Anna
# Scores: [78.0, 85.0, 91.0]
# Minimum: 78.00
# Maximum: 91.00
# Mean: 84.67
#
# Use:
# input()
# float()
# list
# min()
# max()
# sum()
# len()
# f-strings


# ============================================================
# Task 13 — Multiple Assignment
# ============================================================

print("Task 13 — Multiple Assignment")

# TODO:
# Assign these three values using ONE statement:
#
# x = 10
# y = 20
# z = 30

x,y,z = int(input('enter x: ')),int(input('enter y: ')),int(input('enter z: '))


# TODO:
# Print x, y, and z.

print(x,y,z)

# TODO:
# Swap a and b using one Python statement.

a = 5
b = 10

print(a,b)

a, b = b, a

# Expected after swapping:
# a = 10
# b = 5


print(a,b)

# ============================================================
# Task 14 — String Methods
# ============================================================

print("Task 14 — String Methods")

text = "  Python Programming Course  "

# TODO:
# Print the text:
#

text_1 = text.strip()
print(text.strip(), text_1.lower(), text_1.upper(), text_1.replace('Course', 'Lab'), sep='\n')


# 1. without surrounding spaces
# 2. in lowercase
# 3. in uppercase
# 4. with "Course" replaced by "Lab"

# TODO:
# Check and print whether the cleaned text:
#
print(text_1.startswith('Python'))
print(text_1.endswith('Course'))
print(text_1.endswith('Lab'))

# starts with "Python"
# ends with "Course"
#
# Use:
# strip()
# lower()
# upper()
# replace()
# startswith()
# endswith()



# ============================================================
# Task 15 — Boolean Expressions
# ============================================================

print("Task 15 — Boolean Expressions")

age = 22
score = 85
is_master_student = True

# TODO:
# Print the result of:

print(age >= 18) #True
print(score >= 60) #True
print(score >= 60 and is_master_student) #True
print(score < 60 or age < 18) #False
print(not is_master_student) #False

# TODO:
# Predict and then print:

print('the second part:')

print(bool(0))
print(bool(1)) #True
print(bool("")) #False - empty
print(bool("Python")) #False - ?? - not empty => not False => True
print(bool([])) #False - empty => 0 => False
print(bool([1, 2])) #False - ?? - not empty => not False => True


print()

# ============================================================
# Task 16 — Membership
# ============================================================

print("Task 16 — Membership")

numbers = [10, 20, 30]
text = "Python Programming"
student = {
    "name": "Anna",
    "age": 22,
}

# TODO:
# Print the result of:

print(20 in numbers) #True
print(50 not in numbers) #True
print("Python" in text) #True
print("Java" not in text) #True
print("age" in student) #True
print("email" in student) #False


print()

# ============================================================
# Task 17 — Time Decomposition
# ============================================================

print("Task 17 — Time Decomposition")

# Ask the user to enter a duration in seconds.
#
# Example:
# 9374
#
duration=int(input('enter a duration in seconds: '))
# Convert it into:
hours=minutes=seconds=0

# hours
# minutes
# seconds
#

#duration = hours * 60 * 60 + minutes * 60  + sec
#duration//60 = hours * 60 + minutes
#(duration//60)//60 = hours
#sec = duration -hours*60*60 - minutes * 60

hours = (duration//60)//60
print(hours)
minutes = duration//60 - hours * 60
print(minutes)
seconds = duration - hours * 60*60 - minutes*60
print(seconds)

print(f"{duration} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")

# Expected:
# 9374 seconds = 2 hour(s), 36 minute(s), 14 second(s)
#
# Use only:
# int()
# //
# %
# arithmetic
# f-strings

total_seconds = 0

# TODO:
# Read total_seconds from the user.

hours = 0
remaining_seconds = 0
minutes = 0
seconds = 0

# TODO:
# Calculate all four values.

# TODO:
# Print the formatted result.


print()


# ============================================================
# Task 18 — Order Invoice
# ============================================================

print("Task 18 — Order Invoice")

# A customer buys three different products.
#
# Ask for:
# product 1 price and quantity
# product 2 price and quantity
# product 3 price and quantity

price_1, quantity_1 = float(input('enter product 1 price: ')), int(input('enter product 1 quantity: '))
price_2, quantity_2 = float(input('enter product 2 price: ')), int(input('enter product 2 quantity: '))
price_3, quantity_3 = float(input('enter product 3 price: ')), int(input('enter product 3 quantity: '))


#
# Calculate:
# subtotal for every product
# total before tax
# tax = 5%
# final total

subtotal=price_1*quantity_1+price_2*quantity_2+price_3*quantity_3
tax=subtotal*0.05
total = subtotal+tax
print()
print()
print(f"Product 1: {price_1*quantity_1:.2f}",
      f"Product 2: {price_2*quantity_2:.2f}",
      f"Product 3: {price_3*quantity_3:.2f}", sep='\n')
print(30*'-')
print(f"Subtotal: {subtotal:.2f}", f"Tax: {tax:.2f}", f"Total: {total:.2f}", sep='\n')

#
# Example output:
#
# Product 1: 1200.00
# Product 2: 750.00
# Product 3: 400.00
# --------------------
# Subtotal: 2350.00
# Tax: 117.50
# Total: 2467.50
#
# Do not use if, loops, or functions.


# TODO:
# Read all six values.



# TODO:
# Perform the calculations.

# TODO:
# Print a clean invoice using f-strings.


print()

# ============================================================
# Task 19 — Coordinate Analysis
# ============================================================

from math import sqrt as sqrt

print("Task 19 — Coordinate Analysis")

# Ask the user for two points:
#
# (x1, y1)
# (x2, y2)

x1, y1 = float(input("enter the first point's x: ")), float(input("enter the first point's y: "))
x2, y2 = float(input("enter the second's point's x: ")),float(input("enter the second point's y: "))
#
# Store each point as a tuple.
#
point_1=(x1, y1)
point_2=(x2, y2)

print(type(point_1))

# Calculate:


# squared distance

# distance
#
# Formula:
#
# distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
# Print both points and the calculated distance.



# TODO:
# Read the four coordinates.


# TODO:
# Create the two tuples.

delta_x = x2 - x1
delta_y = y2 - y1
distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
distance = sqrt(distance_squared)
#print(point_1, point_2, delta_x, delta_y, distance_squared, f'{distance:.2f}')

# TODO:
# Perform the calculations.

# TODO:
# Print the result with two decimal places.


print(f"difference in x: {delta_x:.2f}", f"difference in y: {delta_y:.2f}", sep='\n')
print(f"distance: {distance:.2f}")

# squared distance
# distance
#

print()


# ============================================================
# Task 20 — Working with Complex Numbers
# ============================================================

print("Task 20 — Complex Numbers")

# Section 2 includes Python's basic data types.
# One numerical type that is easy to forget is complex.
#
# Given:

z1 = 3 + 4j
z2 = 2 - 1j

# TODO:
# Print:
#
print(z1) #3+4j
print(z2) #2-1j
print(type(z1)) #complex number
print(z1 + z2) #5+3j
print(z1 - z2) #1+5j
print(z1 * z2) #(3+4j)(2-1j)=6-3j+8j+4=  10+5j
print(z1 / z2) # (3+4j)/(2-1j) - ?? - 0?4+2?2j
#
# Also print:
#
print(z1.real) #3
print(z1.imag) #4
print(z2.real) #2
print(z2.imag) #-1
# Predict the type of each arithmetic result before running it.


print()



# ============================================================
# Task 21 — Student Data Record
# ============================================================

print("Task 21 — Student Data Record")

# Ask the user for:
#
# name
# age
# university
# first score
# second score
# third score
#
# Store the scores in a list.
#
# Store all student information in a dictionary:
#
# {
#     "name": ...,
#     "age": ...,
#     "university": ...,
#     "scores": [...]
# }
#
# Then calculate:
#
# number of scores
# minimum score
# maximum score
# mean score
#
# Print a formatted student report.
#
# Do not use loops.

student_name = input('enter your name: ')
student_age = int(input('enter your age: '))
university = input('enter your university: ')

score_1 = float(input('enter a first score: '))
score_2 = float(input('enter a second score: '))
score_3 = float(input('enter a third score: '))

scores = [score_1, score_2, score_3]
student = {'name': student_name, 'age': student_age, 'scores': scores}

#print(student['name'])

# TODO:
# Read the values.

# TODO:
# Create scores.

# TODO:
# Create student.

score_count = sum(scores)
minimum_score = min(scores)
maximum_score = max(scores)
mean_score = score_count/len(scores)

# TODO:
# Calculate the statistics.

#print(score_count, minimum_score, maximum_score, mean_score)

# TODO:
# Print a clean report.
print('-'*30)
print('Report:')
print('-'*30)

print(f'Name: {student["name"]}', f"Age: {student['age']}", f"Scores: {student['scores']}", sep='\n')

print('-'*30)

print(f"Mean score: {mean_score:.2f}", f"Maximum score: {maximum_score}", f"Minimum score: {minimum_score}", sep='\n')
print('-'*30)



# ============================================================
# Task 22 — Debug the Program
# ============================================================

print("Task 22 — Debug the Program")

# The program below is supposed to calculate the average
# of three scores entered by the user.
#
# It currently contains several problems.
#
# Find and fix them.
#
# Do NOT use if, try-except, loops, or functions.
#
# Think about:
# - input() types
# - variable names
# - arithmetic
# - operator precedence
# - PEP 8
# - formatted output


# score1=input("Score 1: ")
# Score2=input("Score 2: ")
# score3=input("Score 3: ")
# total=score1+Score2+score3
# average=total/3
# print("Average:"+average)


# TODO:
# Rewrite the program correctly below.

score_1=int(input("Score 1: "))
score_2=int(input("Score 2: "))
score_3=int(input("Score 3: "))
total = score_1 + score_2 + score_3
average = total / 3
print("Average:", average)
