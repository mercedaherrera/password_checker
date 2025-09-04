# Simple Password Strength Checker

password = input("Enter a password to check:")

strength = 0

# Check length
if len(password) >= 8:
    strength += 1

# Check for numbers

if any(char.isdigit() for char in password):
    strength += 1

# Check for uppercase

if any(char.isupper() for char in password):
    strength += 1

# Check for special characters

special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"
if any(char in special_characters for char in password):
    strength += 1

#Feedback

if strength <= 1:
    print("Weak Password")
elif strength == 2:
    print("Medium Password")
else:
    print("Strong Password")
