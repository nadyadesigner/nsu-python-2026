print('  ============================================================')
print(' Task 1 — Countdown with while')
print('  ============================================================')
# Ask the user for a positive integer.
#
# Use a while loop to print from that number down to 1.
# Then print:
#   Go!
#
# Example:
# Input: 5
# Output:
# 5
# 4
# 3
# 2
# 1
# Go!
#
# Make sure the loop variable changes.

# Write your code below:
import time

countdown = int(input('enter your number: '))
while countdown != 0:
    print(countdown)
    time.sleep(1)
    countdown-=1
print('Go!')

print(' ============================================================')
print('Task 2 — Repeat until zero')
print('============================================================')
# Repeatedly ask the user to enter an integer.
#
# Stop when the user enters 0.
#
# Before 0 is entered:
#   count how many non-zero numbers were entered;
#   calculate their sum.
#
# At the end print:
#   Count: ...
#   Sum: ...
#
# Example:
# Input: 5, -2, 7, 0
# Count: 3
# Sum: 10
# Write your code below:

sum = count = 0
number = int(input('enter your number: '))
while number != 0:
    count += 1
    sum += number
    number = int(input('enter your number: '))
print(f"Count: {count}", f"Sum: {sum}", sep='\n')



print('============================================================')
print('Task 3 — Valid input with while True')
print('============================================================')
# Repeatedly ask the user for an integer from 1 to 10.
#
# If the value is outside this range:
#   print "Invalid value"
#   ask again.
#
# When the user enters a valid value:
#   print "Accepted"
#   stop the loop with break.
#
# Required:
# Use:
#   while True
#   break

# Write your code below:

while True:
    number = int(input('enter integer number from 1 to 10: '))
    if number <= 0 or number >= 11:
        print('Invalid value')
#        number = int(input('enter integer number from 1 to 10: '))
    if 0 < number <= 10:
        print('Accepted')
        break




print(' ============================================================')
print(' Task 4 — continue in a while loop')
print(' ============================================================')
# Use a while loop to process numbers from 1 through 20.
#
# Skip numbers divisible by 3 using continue.
# Print all other numbers.
#
# IMPORTANT:
# Update the loop variable correctly so you do not create
# an infinite loop.

# Write your code below:

i = 0
while i <= 20:
    i += 1
    if i % 3 == 0:
        continue
    print(i)



print('============================================================')
print('Task 5 — Search with loop else')
print('============================================================')
numbers = [4, 8, 12, 16, 21, 24]

# Search for the first odd number.
#
# If an odd number is found:
#   print "First odd number: <value>"
#   stop using break.
#
# If the loop finishes without finding any odd number:
#   print "All values are even"
#
# Required:
# Use:
#   for
#   break
#   else

# Write your code below:

for i in numbers:
    if i % 2 != 0:
        print('The first odd number is: ', i)
        break



print('============================================================')
print('Task 6 — Multiplication table with nested loops')
print('============================================================')
# Use nested for loops to print a 5 x 5 multiplication table.
#
# Rows: 1 through 5
# Columns: 1 through 5
#
# Example first row:
# 1 2 3 4 5
#
# Example second row:
# 2 4 6 8 10
#
# Hint:
# Build each row using print(..., end=" ") and print().

# Write your code below:

for row in range(1,6):
    for colomn in range(1,6):
        print(row * colomn, end=' ')
    print()





print('============================================================')
print('Task 9 — Function: is_even')
print('============================================================')
# Write a function:
#
#   is_even(number)
#
# It should return:
#   True  if number is even
#   False otherwise
#
# Then call it with:
#   4
#   7
#   0
#
# Print the returned results.
#
# IMPORTANT:
# The function must return the Boolean result.
# Do not print from inside the function.

# Write your code below:

def is_even(number):
    if number % 2 == 0:
        return(True)
    elif number % 2 != 0:
        return(False)

print(is_even(6), is_even(4),is_even(7), is_even(0))


print('============================================================')
print('Task 10 — Function: calculate_discount')
print('============================================================')
# Write a function:
#   calculate_discount(price, percent)
# It should return the final price after the discount.
# Formula:
# final_price = price - price * percent / 100
# Test it with:
#   calculate_discount(1000, 15)
#   calculate_discount(250, 20)
# Print each returned result.
# Write your code below:

def calculate_discount(price, percent):
    final_price = price * percent / 100
    return final_price

print(calculate_discount(1000, 15), calculate_discount(250, 20)) #150

print('============================================================')
print('Task 11 — return versus print')
print('============================================================')
# The function below is not useful if later code needs
# to reuse the calculated value:
#
# def rectangle_area(width, height):
#     print(width * height)
#
# Rewrite it so that it RETURNS the area.
#
# Then:
#   store the result for width=5, height=4
#   print the result
#   calculate result * 2 and print it
#
# Goal:
# Demonstrate why return is different from print.

# Write your code below:

def rectangle_area(width, height):
     return(width * height)

print(f"area: {rectangle_area(5,4)}", f"area * 2: {rectangle_area(5,4)*2}", sep='\n')


print('============================================================')
print('Task 12 — Function returning multiple values')
print('===========================================================')
# Write a function:
#
#   min_max(numbers)
#
# It receives a list of numbers.
#
# Use loops and conditions to find:
#   the minimum value
#   the maximum value
#
# Return both values.
#
# Do NOT use:
#   min()
#   max()
#
# Test with:
# values = [7, 2, 9, -1, 5, 12, 3]
#
# Unpack the result into:
#   smallest
#   largest
#
# Then print them.

# Write your code below:

def min_max(numbers):
    smallest = numbers[0]
    largest = numbers[-1]
    for i in numbers:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return(smallest, largest)

values=[7, 2, 9, 5, 12, 3]
print(min_max(values))



print('============================================================')
print('Task 13 — Integrated task: validated average')
print('============================================================')
# Write a function:
#   average(total, count)
# Rules:
#   if count == 0:
#       return None
#   otherwise:
#       return total / count
# Then write a loop that asks the user for count until
# the user enters a value >= 0.
# Ask once for total.
# Call average(total, count).
# If the returned result is None:
#   print "Cannot calculate average"
# Otherwise:
#   print the average with 2 decimal places.
# Required:
# Use:
#   function
#   while loop
#   condition
#   return
#   is None

# Write your code below:



def average(total, count):
    if count == 0:
        return None
    while count != 0:
        return(total/count)

total = float(input('enter total: '))
count = float(input('enter count: '))


if average(total, count) is None:
    print('Cannot calculate average')
else:
    print(f"average is: , {average(total, count):.2f}")




print('============================================================')
print('BONUS Task 14 — Guess the number')
print('============================================================')
# Use:
# secret_number = 37
#
# Repeatedly ask the user to guess the number.
#
# Print:
#   Too low
#   Too high
#   Correct
#
# Stop only when the guess is correct.
#
# Also count how many attempts were needed.
#
# Required:
# Use a while loop.

# Write your code below:

secret_number = 37
attempts = 0
number=0
while number != secret_number:
    attempts += 1
    number=int(input('guess the number: '))
    if number > secret_number:
        print("too high")
    elif number < secret_number:
        print('too low')
print('correct!', 'you needed', attempts, 'attempts')

print('============================================================')
print('BONUS Task 15 — Function-based number statistics')
print('============================================================')
# Write a function:
#
#   number_statistics(numbers)
#
# It should use a loop to count:
#   positive numbers
#   negative numbers
#   zeros
#
# Return all three counts.
#
# Test with:
# data = [3, -1, 0, 8, -5, 0, 2, -9]
#
# Print:
#   Positive: ...
#   Negative: ...
#   Zero: ...
#
# Do not use list comprehensions.

# Write your code below:

def number_statistic(numbers):
    positives = negatives = zeros = 0
    for i in numbers:
        if i > 0:
            positives += 1
        elif i == 0:
            zeros += 1
        elif i < 0:
            negatives += 1
    return('positive: ', positives, 'negative: ', negatives, 'zero: ', zeros)

data = [3, -1, 0, 8, -5, 0, 2, -9]
print(number_statistic(data))


print('============================================================')
print('Task 16 — Sum of even numbers with while')
print('============================================================')
# Ask the user for a positive integer n.
#
# Use a while loop to calculate the sum of all even numbers
# from 1 through n.
#
# Example:
# Input: 10
# Even sum: 30
#
# Because:
# 2 + 4 + 6 + 8 + 10 = 30
#
# Required:
# Use a while loop.
#
# Write your code below:

sum = 0
number = int(input('enter integer number: '))
for i in range(1, number + 1):
    sum += i
print(sum)

