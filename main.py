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



