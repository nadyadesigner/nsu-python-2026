# ============================================================
# Task 1 — Built-in Functions
# ============================================================

print("Task 1 — Built-in Functions")
values = [12, 7, 19, 5, 14]
print(len(values))
print(min(values))
print(max(values))
print(sum(values))
print(sum(values)/len(values))
print()


# ============================================================
# Task 2 — Absolute Value and Rounding
# ============================================================

print("Task 2 — Absolute Value and Rounding")

temperature_change = -7.438
measurement = 19.87654
print(abs(temperature_change))
print(round(temperature_change, 1))
print(round(temperature_change, 2))
print(round(temperature_change, 3))
print()


# ============================================================
# Task 3 — Assignment and Augmented Assignment
# ============================================================

print("Task 3 — Assignment and Augmented Assignment")

balance = 1000.0
balance += 250
print(balance)
balance -= 120
print(balance)
balance *= 1.05
print(balance)
balance += 250
balance -= 120
balance *= 1.05
print('The final balance with two decimal places: ', round(balance, 2))
print()

# ============================================================
# Task 4 — Operator Precedence
# ============================================================

print("Task 4 — Operator Precedence")
expression_1 = 2 + 3 * 4 #14
expression_2 = (2 + 3) * 4 #20
expression_3 = 20 / 5 + 3 #7
expression_4 = 20 / (5 + 3) #20/8 = 2,5
expression_5 = 2 ** 3 ** 2 #64 is uncorrect, correct is 512!
print(expression_1, expression_2, expression_3, expression_4, expression_5)
print(expression_1+expression_2+expression_3+expression_4+expression_5)


# ============================================================
# Task 5 — Time Conversion
# ============================================================

print("Task 5 — Time Conversion")

total_seconds = int(input('enter a number of seconds: '))
minutes=total_seconds//60
remaining_seconds=total_seconds-minutes*60
print(minutes, 'minute(s)', 'and', remaining_seconds, 'second(s)')
print()

# ============================================================
# Task 6 — Conversion Is Not Always Reversible
# ============================================================

print("Task 6 — Type Conversion")
value = 17.95
print(int(value))
integer_value = int(value)
float_value = float(value)
print(float_value)
str_value=str(value)
print(str_value, str_value[3], sep='\n')
print(type(str(value)))


# ============================================================
# Task 7 — Basic String Operations
# ============================================================

print("Task 7 — Basic String Operations")

first_name = input("First name: ")
last_name = input("Last name: ")
full_name = first_name + ' ' + last_name + ' '
print(full_name)
print(len(full_name))
print(full_name[0])
print(full_name[-1])
print(full_name[0:3])
full_name3=full_name * 3
print(full_name3)

# ============================================================
# Task 8 — Useful print() Options
# ============================================================

print("Task 8 — Useful print() Options")
language = "Python"
course = "AI and Big Data Analytics"
university = "NSU"
print(language, course, university, sep=' | ')
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
student = {'name': 'Anna', 'age': 22, 'skills': ["Python", "Math", "English"], 'university': 'NSU'}
print(student['name'])
print(student['university'])
print(student['skills'][0], student['skills'][1], sep='\n')
print(len(student['skills']))

 ============================================================
# Task 10 — Mutable and Immutable Objects
# ============================================================

print("Task 10 — Mutable and Immutable Objects")
numbers = [10, 20, 30]
same_numbers = numbers
numbers.insert(0, 99)
print(numbers, same_numbers)
text = "Python"
same_text = text
new_text=text+' '+"Course"
print(text, same_text, new_text, sep='\n')
print()


# ============================================================
# Task 11 — Small Statistics Report
# ============================================================

print("Task 11 — Small Statistics Report")

scores = [78, 92, 85, 69, 88]
number = len(scores)
min_scores = min(scores)

max_scores = max(scores)
sum_scores = sum(scores)
mean_score=sum(scores)/len(scores)
print(f" Number of scores: {number}\n",
    f"Minimum: {min_scores}\n",
    f"Maximum: {max_scores}\n",
    f"Mean: {mean_score}\n")



# ============================================================
# Task 12 — PEP 8 Cleanup
# ============================================================

print("Task 12 — PEP 8 Cleanup")
Price = 1250
Quantity = 3
Discount_percent = 10
Total_price = Price * Quantity - Discount_percent / 100 * Price * Quantity
print("Final price is: ",Total_price)

# ============================================================
# Optional Challenge — Student Score Summary
# ============================================================

print("Optional Challenge — Student Score Summary")
name=input('enter your name: ')

score_1, score_2, score_3 = float(input('enter a first score ')), float(input('enter a second score ')), float(input('enter a third score '))
scores=[score_1, score_2, score_3]
min_score=min(scores)
max_score=max(scores)
mean_score=sum(scores)/len(scores)
print(f"Student: {name}",
      f"Scores: {scores}", f"Minimum: {min_score}", f"Maximum: {max_score}",
      f"Mean: {mean_score:.2f}", sep='\n')


# ============================================================
# Task 13 — Multiple Assignment
# ============================================================

print("Task 13 — Multiple Assignment")
x,y,z = int(input('enter x: ')),int(input('enter y: ')),int(input('enter z: '))
print(x,y,z)
a = 5
b = 10
print(a,b)
a, b = b, a
print(a,b)

# ============================================================
# Task 14 — String Methods
# ============================================================

print("Task 14 — String Methods")
text = "  Python Programming Course  "
text_1 = text.strip()
print(text.strip(), text_1.lower(), text_1.upper(), text_1.replace('Course', 'Lab'), sep='\n')
print(text_1.startswith('Python'))
print(text_1.endswith('Course'))
print(text_1.endswith('Lab'))

# ============================================================
# Task 15 — Boolean Expressions
# ============================================================

print("Task 15 — Boolean Expressions")

age = 22
score = 85
is_master_student = True
print(age >= 18) #True
print(score >= 60) #True
print(score >= 60 and is_master_student) #True
print(score < 60 or age < 18) #False
print(not is_master_student) #False
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
duration=int(input('enter a duration in seconds: '))
hours=minutes=seconds=0
hours = (duration//60)//60
print(hours)
minutes = duration//60 - hours * 60
print(minutes)
seconds = duration - hours * 60*60 - minutes*60
print(seconds)
print(f"{duration} seconds = {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
print()


# ============================================================
# Task 18 — Order Invoice
# ============================================================

print("Task 18 — Order Invoice")
price_1, quantity_1 = float(input('enter product 1 price: ')), int(input('enter product 1 quantity: '))
price_2, quantity_2 = float(input('enter product 2 price: ')), int(input('enter product 2 quantity: '))
price_3, quantity_3 = float(input('enter product 3 price: ')), int(input('enter product 3 quantity: '))
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

print()

# ============================================================
# Task 19 — Coordinate Analysis
# ============================================================

from math import sqrt as sqrt

print("Task 19 — Coordinate Analysis")
x1, y1 = float(input("enter the first point's x: ")), float(input("enter the first point's y: "))
x2, y2 = float(input("enter the second's point's x: ")),float(input("enter the second point's y: "))
point_1=(x1, y1)
point_2=(x2, y2)
print(type(point_1))
delta_x = x2 - x1
delta_y = y2 - y1
distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2
distance = sqrt(distance_squared)
print(f"difference in x: {delta_x:.2f}", f"difference in y: {delta_y:.2f}", sep='\n')
print(f"distance: {distance:.2f}")
print()


# ============================================================
# Task 20 — Working with Complex Numbers
# ============================================================

print("Task 20 — Complex Numbers")

z1 = 3 + 4j
z2 = 2 - 1j

print(z1) #3+4j
print(z2) #2-1j
print(type(z1)) #complex number
print(z1 + z2) #5+3j
print(z1 - z2) #1+5j
print(z1 * z2) #(3+4j)(2-1j)=6-3j+8j+4=  10+5j
print(z1 / z2) # (3+4j)/(2-1j) - ?? - 0?4+2?2j

print(z1.real) #3
print(z1.imag) #4
print(z2.real) #2
print(z2.imag) #-1
print()



# ============================================================
# Task 21 — Student Data Record
# ============================================================

print("Task 21 — Student Data Record")
student_name = input('enter your name: ')
student_age = int(input('enter your age: '))
university = input('enter your university: ')
score_1 = float(input('enter a first score: '))
score_2 = float(input('enter a second score: '))
score_3 = float(input('enter a third score: '))
scores = [score_1, score_2, score_3]
student = {'name': student_name, 'age': student_age, 'scores': scores}
score_count = sum(scores)
minimum_score = min(scores)
maximum_score = max(scores)
mean_score = score_count/len(scores)
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
score_1=int(input("Score 1: "))
score_2=int(input("Score 2: "))
score_3=int(input("Score 3: "))
total = score_1 + score_2 + score_3
average = total / 3
print("Average:", average)
