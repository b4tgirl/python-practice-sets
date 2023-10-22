# Integer
a = 5

# Float
b = 2.5

# String
c = "Hello, World!"

# Boolean
d = True

# List
e = [1, 2, 3, 4, 5]

# Tuple
f = (1, 2, 3, 4, 5)

# Set
g = {1, 2, 3, 4, 5}

# Dictionary
h = {'a': 1, 'b': 2, 'c': 3}

# Printing the types and values
print(f"Variable a is of type: {type(a)}, value: {a}")
print(f"Variable b is of type: {type(b)}, value: {b}")
print(f"Variable c is of type: {type(c)}, value: {c}")
print(f"Variable d is of type: {type(d)}, value: {d}")
print(f"Variable e is of type: {type(e)}, value: {e}")
print(f"Variable f is of type: {type(f)}, value: {f}")
print(f"Variable g is of type: {type(g)}, value: {g}")
print(f"Variable h is of type: {type(h)}, value: {h}")


# Taking input from the user
name = input("Please enter your name: ")

# Printing the welcome message
print(f"Welcome, {name}!")

# Taking input from the user for Celsius temperature
celsius = float(input("Enter temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Printing the converted temperature in Fahrenheit
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")

import math

# Read the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter
diameter = 2 * radius

# Calculate perimeter (circumference)
perimeter = 2 * math.pi * radius

# Calculate area
area = math.pi * radius ** 2

# Print the results
print(f"Given the radius {radius}:")
print(f"Diameter of the circle is: {diameter}")
print(f"Perimeter of the circle is: {perimeter:.2f}")
print(f"Area of the circle is: {area:.2f}")

# Ternary Operator
x = 10
y = 20
max_value = x if x > y else y
print(f"The maximum value is: {max_value}")

# Bitwise Operators
# Assume a=5, b=6

a = 5
b = 6

# Binary AND
binary_and = a & b
print(f"Binary AND of {a} and {b} is: {binary_and}")

# Binary OR
binary_or = a | b
print(f"Binary OR of {a} and {b} is: {binary_or}")

# Binary XOR
binary_xor = a ^ b
print(f"Binary XOR of {a} and {b} is: {binary_xor}")

# Negation
negation_a = ~a
negation_b = ~b
print(f"Negation of {a} is: {negation_a}")
print(f"Negation of {b} is: {negation_b}")

# Left Shift
left_shift_a = a << 2
print(f"Left shift of {a} by 2 positions is: {left_shift_a}")

# Right Shift
right_shift_b = b >> 2
print(f"Right shift of {b} by 2 positions is: {right_shift_b}")

# Program to print the largest of three numbers

# Taking input for three numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Using if-elif-else statements to find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Printing the largest number
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")

# Program to check if a person is eligible for driving

# Define the eligible driving age
eligible_age = 18

# Taking input for the person's age
age = int(input("Enter your age: "))

# Checking eligibility using if-else statement
if age >= eligible_age:
    print("You are eligible for driving.")
else:
    print(f"Sorry, you are not eligible for driving. You need to be at least {eligible_age} years old.")

# Program to check if a given number is odd or even

# Taking input from the user
number = int(input("Enter a number: "))

# Checking if the number is odd or even
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

# Python code to print the grade of a student based on the marks

# Taking input for the marks obtained by the student
marks = float(input("Enter the marks obtained: "))

# Checking the grade using elif statements
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'F'

# Printing the grade of the student
print(f"The grade for the marks {marks} is {grade}.")


# Python program to accept semester number and roll number from an M.Sc. student

# Valid semester numbers and roll numbers
valid_semesters = [1, 2, 3, 4]
valid_roll_numbers = list(range(1, 31))

# Taking input for semester number and roll number
semester = int(input("Enter semester number: "))
roll_number = int(input("Enter roll number: "))

# Checking for valid inputs and displaying remarks accordingly
if semester in valid_semesters and roll_number in valid_roll_numbers:
    print("Remarks by subject experts:")
    if semester == 1:
        print("Semester 1 remarks.")
    elif semester == 2:
        print("Semester 2 remarks.")
    elif semester == 3:
        print("Semester 3 remarks.")
    elif semester == 4:
        print("Semester 4 remarks.")
else:
    print("Invalid inputs! Please enter valid semester number (1, 2, 3, or 4) and roll number (1 to 30).")


def computegrade(score):
    if score > 1.0 or score < 0.0:
        return "Score is out of range!"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

# Taking input for the score from the user
score = float(input("Enter the score: "))

# Computing and printing the grade
grade = computegrade(score)
print(f"The grade for the score {score} is {grade}.")


# Demonstrating various built-in functions in Python

# 1. input()
name = input("Enter your name: ")

# 2. oct()
oct_value = oct(10)

# 3. hex()
hex_value = hex(255)

# 4. pow()
power_value = pow(2, 3)

# 5. print()
print("Hello, world!")

# 6. range()
range_values = list(range(1, 5))

# 7. reversed()
reversed_list = list(reversed(range_values))

# 8. round()
rounded_value = round(3.6)

# 9. issubclass()
issubclass_bool = issubclass(bool, int)

# 10. str()
str_value = str(123)

# 11. type()
type_value = type(10)

# 12. abs()
absolute_value = abs(-7)

# 13. all()
all_values = all([True, True, False])

# 14. bin()
binary_value = bin(5)

# 15. bool()
bool_value = bool(1)

# 16. sum()
sum_value = sum([1, 2, 3, 4, 5])

# 17. ascii()
ascii_value = ascii('hello')

# 18. eval()
eval_value = eval('2 + 3')

# 19. format()
formatted_value = format(123, 'd')

# 20. len()
length = len("Hello, world!")

# 21. list()
list_values = list((1, 2, 3))

# 22. object()
object_value = object()

# 23. open()
file = open('example.txt', 'r')

# 24. complex()
complex_value = complex(3, 4)

# 25. dir()
dir_values = dir(list)

# 26. divmod()
divmod_values = divmod(9, 2)

# 27. min()
minimum_value = min(4, 5, 1, 9, 2)

# 28. set()
set_values = set([1, 2, 3, 4, 4, 5])

# 29. sorted()
sorted_values = sorted([5, 4, 3, 2, 1])

# 30. next()
iterator = iter(range(3))
next_value = next(iterator)

# Printing the results
print(name, oct_value, hex_value, power_value, range_values, reversed_list, rounded_value, issubclass_bool, str_value, type_value, absolute_value, all_values, binary_value, bool_value, sum_value, ascii_value, eval_value, formatted_value, length, list_values, object_value, complex_value, dir_values, divmod_values, minimum_value, set_values, sorted_values, next_value)


# Finding absolute values of given numbers

# Given numbers
numbers = [-10, 20, 3.44, -1.6]

# Finding absolute values
absolute_values = [abs(num) for num in numbers]

# Printing the absolute values
for i in range(len(numbers)):
    print(f"The absolute value of {numbers[i]} is {absolute_values[i]}")


# Finding binary representations of the given numbers

# Given numbers
numbers = [25, 14]

# Finding binary representations
binary_representations = [bin(num) for num in numbers]

# Printing the binary representations
for i in range(len(numbers)):
    print(f"The binary representation of {numbers[i]} is {binary_representations[i]}")


# Converting string to bytes

# Given string
my_string = "Welcome to DBS"

# Converting the string to bytes
bytes_string = my_string.encode()

# Printing the bytes representation
print(f"The bytes representation of the string is: {bytes_string}")


# Finding the sum of given numbers

# Given numbers
numbers = [12, 23, 34, 45, 56]

# Finding the sum
total_sum = sum(numbers)

# Printing the sum
print(f"The sum of the numbers {', '.join(map(str, numbers))} is {total_sum}.")

# Given strings
strings = ["Hello", "Python", "OpenAI", "Artificial Intelligence"]

# Finding lengths of the strings
lengths = [len(s) for s in strings]

# Printing the lengths
for i in range(len(strings)):
    print(f"The length of '{strings[i]}' is {lengths[i]}.")

# Converting numbers into complex numbers

# Given numbers
numbers = [3, 4, 5, 6, 7]

# Converting into complex numbers
complex_numbers = [complex(num, 0) for num in numbers]

# Printing the complex numbers
for i in range(len(numbers)):
    print(f"The complex representation of {numbers[i]} is {complex_numbers[i]}.")


# Building a set from given input values

# Given input values
input_values = [1, 2, 3, 4, 5, 2, 3, 4, 6, 7, 8, 9, 1]

# Building a set
input_set = set(input_values)

# Printing the set
print(f"The set of input values is: {input_set}")

# Finding the hexadecimal equivalent of a decimal number

# Given decimal number
decimal_number = 255

# Finding the hexadecimal equivalent
hexadecimal_equivalent = hex(decimal_number)

# Printing the hexadecimal equivalent
print(f"The hexadecimal equivalent of {decimal_number} is {hexadecimal_equivalent}.")


# Arrange letters in a string alphabetically

# Given string
my_string = "helloopenai"

# Arrange the letters alphabetically
arranged_string = ''.join(sorted(my_string))

# Print the arranged string
print(f"The string '{my_string}' arranged alphabetically is '{arranged_string}'.")

# Reading values entered by the user and printing them

# Reading the first value
value1 = input("Enter the first value: ")

# Reading the second value
value2 = input("Enter the second value: ")

# Printing the values entered by the user
print(f"The values entered by the user are: {value1} and {value2}.")

# Summation of numbers in a list

# Given list of numbers
numbers = [1, 2, 3, 4, 5]

# Counting the summation of numbers in the list
summation = sum(numbers)

# Printing the summation
print(f"The summation of numbers in the list {numbers} is {summation}.")


# Calculating average, max, and min numbers in a list

# Given list of numbers
numbers = [12, 23, 34, 45, 56, 67]

# Calculating the average
average = sum(numbers) / len(numbers)

# Calculating the maximum and minimum numbers
max_number = max(numbers)
min_number = min(numbers)

# Printing the results
print(f"The average of numbers in the list is {average}.")
print(f"The maximum number in the list is {max_number}.")
print(f"The minimum number in the list is {min_number}.")
