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


