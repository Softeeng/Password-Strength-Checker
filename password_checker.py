def check_password_strength(password):
    # Start here - just check the length
    length = len(password)

    if length < 8:
        return "Too short"
    

    # Check if password has uppercase and lowercase letters, numbers, and special characters
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    # Score password
    score = sum([has_upper, has_lower, has_digit, has_special])
    if score == 4 and length >= 12:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"

# Loop until password is acceptable
while True:
    password = input("Enter a password (or 'q' to quit): ").strip()
    if password.lower() == 'q':
        print("Aborted.")
        break

    result = check_password_strength(password)
    if result in ("Strong", "Very Strong"):
        print(f"Password accepted: {result}")
        break
    else:
        print(f"Password not accepted: {result}. Please try again")
        