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


