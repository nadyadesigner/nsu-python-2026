

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

