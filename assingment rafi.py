#Largest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
if b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)




# Quadrant identifier
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("1st Quadrant")
if x < 0 and y > 0:
    print("2nd Quadrant")
if x < 0 and y < 0:
    print("3rd Quadrant")
if x > 0 and y < 0:
    print("4th Quadrant")
if x == 0 and y == 0:
    print("Origin")
else:
    print("On Axis")





# Age classfier
age = int(input("Enter your age: "))

if age <= 1:
    print("Infant")
if age <= 3:
    print("Toddler")
if age <= 12:
    print("Child")
if age <= 19:
    print("Teenager")
else:
    print("Adult")





#Bmi calculator

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")
if bmi < 25:
    print("Normal")
if bmi < 30:
    print("Overweight")
else:
    print("Obese")




    # Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", num1 + num2)
if op == '-':
    print("Result:", num1 - num2)
if op == '*':
    print("Result:", num1 * num2)
if op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")





# FizzBuzz (for loop)
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    else:
        print(i)



# Armstrong number checker
num = int(input("Enter a number: "))
sum = 0
temp = num
n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")








#Number Reverser
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number is:", reverse)





#Sum of digits
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits is:", total)






# print the pattern
for i in range(1, 6):
    print(str(i) * i)




    
