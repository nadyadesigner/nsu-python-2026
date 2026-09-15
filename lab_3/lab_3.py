# ============================================================
print('='*30)
print('Task 1 — Positive, negative, or zero')
# ============================================================
# Ask the user to enter an integer.
# Print exactly one of:
#   Positive
#   Negative
#   Zero
#
# Example:
# Input: -7
# Output: Negative

# Write your code below:

number = int(input('enter your number: '))
if number > 0:
    print('Positive')
elif number == 0:
    print('Zero')
elif number < 0:
    print('Negative')

print('='*30)
# ============================================================
print('Task 2 — Age category')
# ============================================================
# Ask the user for their age.
#
# Print:
#   Child      -> age < 13
#   Teenager   -> 13–17
#   Adult      -> 18–64
#   Senior     -> 65 or older
#
# Test boundary values: 12, 13, 17, 18, 64, 65.

# Write your code below:

age=int(input('enter your age: '))
if age < 13:
    print('child')
elif 13<= age <=17:
    print('teenager')
elif 18<= age <= 64:
    print('adult')
elif age >= 65:
    print('senior')

print('='*30)
# ============================================================
print('Task 3 — Grade classifier')
# ============================================================
# Ask the user for a score.
#
# First check whether the score is between 0 and 100 inclusive.
#
# For a valid score:
#   A    -> 90–100
#   B    -> 75–89
#   C    -> 60–74
#   Fail -> below 60
#
# For an invalid score print:
#   Invalid score

# Write your code below:

print('='*30)
# ============================================================
print('Task 4 — Access decision')
# ============================================================
# Ask the user for:
#   age
#   whether they have a ticket: yes/no
#
# A person may enter only if:
#   age >= 18 AND they have a ticket.
#

age=int(input('enter your age: '))
if age < 18:
    print('must be 18 or older')
if age >= 18:
    ticket = input('do you have a ticket? (only "yes" or "no"): ')
    if ticket == 'yes':
        print('access granted')
    if ticket != 'yes':
        print('ticket required')
# Print one of:
#   Access granted
#   Ticket required
#   Must be 18 or older

# Write your code below:

print('='*30)
# ============================================================
print('Task 5 — Even numbers with range()')
# ============================================================
# Print all even numbers from 2 through 30.
#
# Required:
# Use range(start, stop, step).

# Write your code below:

for i in range(2,31):
    print(i)

print('='*30)
# ============================================================
print('Task 6 — Sum of multiples of 3')
# ============================================================
# Calculate and print the sum of all multiples of 3
# from 3 through 99.
#
# Required:
# Use a for loop and an accumulator.
#
# Expected result:
# 1683

# Write your code below:

sum=0
for i in range(3,100,3):
    sum += i
print('The sum of multiplies of 3: ',sum)

print('='*30)
# ============================================================
print('Task 7 — Count number categories')
# ============================================================

numbers = [4, -2, 0, 7, -5, 9, 0, -1, 8]


# Count how many values are:
#   positive
#   negative
#   zero
#
# Print all three counts.
# Do not manually count the values.

# Write your code below:
positives = negatives = zeros = 0

for i in numbers:
    if i > 0:
        positives += 1
    elif i < 0:
        negatives += 1
    elif i == 0:
        zeros += 1
print(f"{positives} values are positive", f"{negatives} values are negative", f"{zeros} 'zero' values", sep='\n')


print('='*30)
