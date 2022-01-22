def add(num1, num2):
	return num1 + num2
	
def subtract(num1, num2):
	return num1 - num2
	
def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

print("Please select operation \n1 for Add \n2 for Subtract \n3 for Multiply \n4 for Divide\n")
operator = int(input("Select operations form 1, 2, 3, 4 :"))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if operator == 1:
	print("Addition of ",n1, "+", n2, "is",add(n1, n2))

elif operator == 2:
	print("Subtraction of ",n1, "-", n2, "is",subtract(n1, n2))

elif operator == 3:
	print("Multiplication of",n1, "*", n2, "is",multiply(n1, n2))

elif operator == 4:
	print("Division of ",n1, "/", n2, "is",divide(n1, n2))
else:
	print("Invalid input")
