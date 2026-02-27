import random

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operator")

    except:
        print("Invalid input!")

def password_generator():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
    length = int(input("Password length: "))
    password = ""

    for i in range(length):
        password += random.choice(chars)

    print("Generated password:", password)

def number_guess():
    secret = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("Guess number (1-20): "))
        attempts += 1

        if guess == secret:
            print("Correct! Attempts:", attempts)
            break
        elif guess < secret:
            print("Too low")
        else:
            print("Too high")

def menu():
    while True:
        print("\n---- Python Mini Tools ----")
        print("1. Calculator")
        print("2. Password Generator")
        print("3. Guess Game")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            password_generator()
        elif choice == "3":
            number_guess()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


menu()

# Created by Amith Ajith Kumar as part of Python practice
