# Take three numbers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Store the numbers in a list
numbers = [num1, num2, num3]

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Display the numbers in descending order with '>' symbols
print(f"{numbers[0]} > {numbers[1]} > {numbers[2]}")

# Identify and print the biggest number
print(f"The biggest number is: {numbers[0]}")
