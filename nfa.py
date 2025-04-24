def has_upper(password):
    return any(c.isupper() for c in password)

def has_lower(password):
    return any(c.islower() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_special(password):
    return any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password)

def is_alphanumeric_or_special(password):
    return all(c.isalnum() or c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password)

def is_long_enough(password):
    return len(password) >= 8

def nfa_checker(password):

    if not has_upper(password):
        print("Password must contain at least one uppercase letter.")
    if not has_lower(password):
        print("Password must contain at least one lowercase letter.")
    if not has_digit(password):
        print("Password must contain at least one digit.")
    if not has_special(password):
        print("Password must contain at least one special characters.")
    if not is_alphanumeric_or_special(password):
        print("Password must contain only alphanumeric or special characters.")
    if not is_long_enough(password):
        print("Password must be at least 8 characters long.")

    if has_upper(password) and has_lower(password) and has_digit(password) and has_special(password) and is_long_enough(password):
        print("Password is valid.")
        return True
    else:
        return False
    

with open("varied_passwords.txt", "r") as file:
    for line in file:
        password = line.strip()
        nfa_checker(password)
        print(f"Password: {password}")
        print("-" * 30)
        print("\n")
