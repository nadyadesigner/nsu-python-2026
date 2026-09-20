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

score = int(input('enter your score: '))
if 0 < score <= 100:
    if score <= 60:
        print("fail")
    elif 60 < score <= 74:
        print('C mark')
    elif 75 <= score <= 89:
        print('B mark')
    elif 90 <= score <= 100:
        print('A mark')

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

print('='*30)

# ============================================================
print('Task 8 — Count vowels')
# ============================================================
# Ask the user to enter a word or short text.
# Count how many vowels it contains.

word=input('enter a word or short text: ')
#
# Treat uppercase and lowercase equally.
# Vowels: a e i o u
#
vowels = 0

for i in word.lower():
    if i in 'aeiou':
        vowels += 1
print(f"{vowels} vowels are in your word '{word}'")

# Example:
# Input: Artificial Intelligence
# Output: 10
#
# Hint:
# Iterate directly over the string.

# Write your code below:

print('='*30)
# ============================================================
print('Task 9 — Student results')
# ============================================================
scores = [85, 42, 67, 91, 58, 73, 100, 39]

# Count:
#   passed students: score >= 60
#   failed students: score < 60
#
# Also print the average score.

passeds = faileds = total = amounts= 0
for i in scores:
    if i >= 60:
        passeds += 1
    elif i < 60:
        faileds += 1
    total += i
    amounts+=1
print(f"passed students: {passeds}", f"failed students: {faileds}", f"Average score: {total/amounts:.2f}", sep='\n')

# ============================================================
print('Task 10 — Search and stop')
# ============================================================
names = ["Anna", "Boris", "Sasha", "Maria", "Oleg", "Dina"]

# Ask the user for a name.
# Search the list using a for loop.
Flag = True
name=input('enter your name: ')
for i in names:
    if name == i:
        Flag = False
        break
if not Flag:
    print('Found')
else:
    print('Not found')

# If found:
#   print "Found"
#   stop immediately with break
#
# If not found:
#   print "Not found"
#
# Do not use:
#   if target in names
#
# Hint:
# A Boolean variable such as found = False can help.

# Write your code below:
print('='*30)


# ============================================================
print('Task 11 — Skip invalid scores')
# ============================================================
print('='*30)
raw_scores = [78, -5, 91, 120, 66, 0, 88, 101, 54]
average_valid = 0
total_valid = 1

# Valid scores are from 0 to 100 inclusive.
#
# Use continue to skip invalid scores.
# For valid scores:
#   print each valid score
#   calculate the average of valid scores

print('Valid scores: ')
for i in raw_scores:
    if 0 <= i <= 100:
        print(i)
        average_valid += i
        total_valid += 1
    else:
        continue

print(f"The average of valid scores: {average_valid/total_valid:.2f}")
# At the end print:
#   Valid scores: ...
#   Average: ...
#
# Required:
# Use continue.

# Write your code below:

print('='*30)
# ============================================================
print('Task 12 — Dictionary iteration')
# ============================================================
print('='*30)
student_scores = {
    "Anna": 92,
    "Boris": 58,
    "Sasha": 76,
    "Maria": 49,
    "Oleg": 84,
}

# Iterate using .items().
#
# Print:
#   Anna: Pass
#   Boris: Fail
#   ...
#
# Score >= 60 means Pass.
# Then print how many students passed.

# Write your code below:

#print(student_scores.items())
passes = 0
for key, value in student_scores.items():
    if value >= 60:
        print(key, ': Pass')
        passes += 1
    elif value < 60:
        print(key, ': Fail')
#    print(key, value)
print(f"{passes} students passed an exam")


print()

print('='*30)
# ============================================================
print('BONUS Task 13 — FizzBuzz')
# ============================================================
print('='*30)
# Print numbers 1 through 30.
#
# If divisible by both 3 and 5 -> FizzBuzz
# If divisible only by 3       -> Fizz
# If divisible only by 5       -> Buzz
# Otherwise print the number.
#
# Hint:
# Check the most specific condition first.

# Write your code below:

divisible_3_5 = divisible_3 = divisible_5 = 0

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        divisible_3_5 += 1
        print('FizzBuzz')
    elif i % 5 == 0:
        divisible_5 += 1
        print('Buzz')
    elif i % 3== 0:
        print('Fizz')
        divisible_3 += 1
    else:
        print(i)

print('.'*30)

print(f"divisible by 3 and 5: {divisible_3_5}", f"divisible by 3: {divisible_3}", f"divisible by 5: {divisible_5}", sep='\n')

print('='*30)


# ============================================================
print('BONUS Task 14 — Limited login attempts')
# ============================================================
print('='*30)
correct_pin = "4821"

# Give the user at most 3 attempts to enter the PIN.
# Use:
#   for
#   range()
#   break
#for i in range(3):
  #  i = int(input(''))
# Correct PIN:
#   Access granted
# Three wrong attempts:
#   Access denied
# Do NOT use a while loop.
# Write your code below:
print('='*30)

for i in range(3):
    password = input('enter password: ')
    if password == correct_pin:
        print('access granted!')
        break
    elif password != correct_pin:
        print('access denied')
        if i == 2:
            print('no attempts anymore')

print('='*30)


# ============================================================
print('EXTRA Task 15 — Largest of three numbers')
# ============================================================
print('='*30)
# Ask the user to enter three integers.
#
# Print the largest number.
#
# Do NOT use:
#   max()
#
# Example:
# Input:
# 12
# 7
# 19
#
# Output:
# Largest: 19
#
# Think carefully about equal values.

max_number = 0
number1, number2, number3 = int(input('enter a first number: ')), int(input('enter a second number: ')), int(input('enter a third number: '))

numbers=[number1, number2, number3]
for i in numbers:
    if i>max_number:
        max_number = i
    else:
        continue
print(f"Maximum number is {max_number}")

print('='*30)
# Write your code below:
#I go through each number and check - the index is greater than my current maximum. If it is, the value of the maximum variable becomes equal to the value of the index.

# ============================================================
print('EXTRA Task 16 — Number statistics')
# ============================================================

numbers = [12, -4, 7, 0, 15, -9, 8, -2, 0, 21]

# Using one for loop, calculate:
#   number of positive values
positives = negatives = zeros = sum_positives = sum_negatives = 0

for i in numbers:
    if i > 0:
        positives += 1
        sum_positives += i
    if i == 0:
        zeros += 1
    if i < 0:
        negatives += 1
        sum_negatives += i
print(f"Positive: {positives}", f"Negatives: {negatives}", f"Zero: {zeros}",
      f"Positive sum {sum_positives}", f"Negative sum: {sum_negatives}",sep='\n')
#   number of negative values
#   number of zeros
#   sum of positive values
#   sum of negative values
#
# Expected:
# Positive: 5
# Negative: 3
# Zero: 2
# Positive sum: 63
# Negative sum: -15
#
# Do not manually calculate the values.

# Write your code below:

print('='*30)


# ============================================================
print('EXTRA Task 17 — Highest and lowest score')
# ============================================================
print('='*30)

scores = [71, 85, 42, 96, 58, 83, 67, 91]

# Find the highest and lowest scores using a for loop.
#
# Do NOT use:
#   max()
#   min()
#   sorted()
#
# Hint:
# Start with:
# highest = scores[0]

# lowest = scores[0]
#
# Expected:
# Highest: 96
# Lowest: 42

# Write your code below:

highest = scores[0]
lowest = scores[0]
for i in scores:
    if i >= highest:
        highest = i
    elif i <= lowest:
        lowest = i
print('the highest: ', highest)
print('the lowest: ', lowest)



print('='*30)
# ============================================================
print('EXTRA Task 18 — Temperature analysis')
# ============================================================
print('='*30)
temperatures = [12, 18, 25, 31, 7, 22, 35, 16, 29, 4]
hots = colds = milds = warms = 0
for i in temperatures:
    if i <= 10:
        print(f"{i}: Cold")
        colds += 1
    if 10 < i <= 19:
        print(f"{i}: Mild")
        milds += 1
    if 20 < i <= 29:
        print(f"{i}: Warm")
        warms += 1
    if i <= 30:
        print(f"{i}: Hot")
        hots +=1
print('.'*30)
print(f"{colds} cold days", f"{milds} mild days", f"{warms} warm days", f"{hots} hot days", sep='\n')

# Classify every temperature:
#
#   Cold -> below 10
#   Mild -> 10–19
#   Warm -> 20–29
#   Hot  -> 30 or above
#
# Example output:
# 12: Mild
# 18: Mild
# 25: Warm
# ...
#
# After processing all temperatures, print how many
# temperatures belong to each category.

# Write your code below:

print('='*30)

