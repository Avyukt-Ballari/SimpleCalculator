num1 = input("What is your First desired number? ")

num2 = input("What is your Second desired number? ")

operation = input("What Operation, would you like? (Sub or Add) ")

if operation == "Add":
    x = float(num1) + float(num2)
elif operation == "Sub":
    x = float(num1) - float(num2)
else: 
    print("The Operation you requested was not found.")

print(x)
