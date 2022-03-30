# Simple Addition

a = int(input("Enter first number: "))
operation = input("Enter operation: ")
b = int(input("Enter second number: "))
flag = True

match operation:
	case "+":
		c = a + b
	case "-":
		c = a - b
	case "*":
		c = a * b
	case "/":
		c = a / b
	case "%":
		c = a % b
	case _:
		print("Invalid operation")
		flag = False

if (flag):
	print("Sum of above two numbers is: " + str(c))