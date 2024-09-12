#!/usr/bin/env python3
def admin_login(username, password):
    # For simplicity, let's assume we have a dictionary of admin users
    admin_users = {"admin": "password"}
    if username in admin_users and admin _users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")
    pass
def hows_the_weather(temperature):
    if temperature > 25:
        print("It's hot!")
    elif temperature > 15:
        print("It's warm!")
    else:
        print("It's cold!")
    pass
def fizzbuzz(num):
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass

def calculator(operation, num1, num2):
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operation.")
    pass