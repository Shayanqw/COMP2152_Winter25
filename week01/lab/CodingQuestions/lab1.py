# Sample Coding Questions 01 Week 01
# Shayan Pourahmad
# Student ID: 101474651

array_variable = [1, 4, 7, 9]

# 2. Order of Operations:
a, b, c, d = 1, 2, 3, 4

# Fully-Bracketed Version, it shoulld print 2.5 :
# e = a * c - b / d :
e = (a * c) - (b / d)
print(e)

# Fully-Bracketed Version should print 0:
e = ((a - ((b ** c) // d)) + (a % c))
print(e)

# 3.Formatting:
# Create a variable called "temperature" with the value 32.6
temperature = 32.6

# print the temperature by 3 number after decimal
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# hold the user input:
userAge = int(input("Please enter your age: "))

# Print the UserAge:
print(f"Now showing the shop items filtered by age: {userAge}")
