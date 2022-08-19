# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print("Select an operation to perform")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input()

if operation == "1":
    num1 = input("Enter first num:")
    num2 = input("Enter second num:")
    print("The sum is"+str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first num:")
    num2 = input("Enter second num:")
    print("The subtraction is" + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first num:")
    num2 = input("Enter second num:")
    print("The multiplication is" + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first num:")
    num2 = input("Enter second num:")
    print("The division is" + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")

