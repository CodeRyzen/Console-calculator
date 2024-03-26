while True:
    action = input("+, -, / or *: ")
    
    if action not in ["+", "-", "/", "*"]:
        print("Please choose a valid operation.")
    else:
        print("OK")
        break

first_number = float(input("Write the first number: "))
second_number = float(input("Write the second number: "))

if action == "+":
    print(f"Result: {first_number} + {second_number} = {first_number + second_number}")
elif action == "-":
    print(f"Result: {first_number} - {second_number} = {first_number - second_number}")
elif action == "/":
    if second_number == 0:
        print("Error: Division by zero!")
    else:
        print(f"Result: {first_number} / {second_number} = {first_number / second_number}")
elif action == "*":
    print(f"Result: {first_number} * {second_number} = {first_number * second_number}")
else:
    print("Invalid operation!")

input("Press Enter to exit")