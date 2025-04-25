import time

def dfa_checker(password):

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$%^&*()-_=+[]{}|;:',.<>?/":
            has_special = True
        else:
            print("Password contains invalid characters.")
            return False
    
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_lower:
        print("Password must contain at least one lowercase letter.")  
    if not has_digit:
        print("Password must contain at least one digit.")
    if not has_special:
        print("Password must contain at least one special character.")

    if has_upper and has_lower and has_digit and has_special:
        print("Password is valid.")
        return True
    else:
        return False

total_time = 0

with open("varied_passwords.txt", "r") as file:
    for line in file:
        
        password = line.strip()
        
        start_time = time.perf_counter()
        dfa_checker(password)
        end_time = time.perf_counter()

        duration_ms = (end_time - start_time) * 1000  # convert to milliseconds
        total_time += duration_ms

        print(f"Password: {password}")
        print(f"Time taken: {duration_ms:.4f} ms")
        print("-" * 30)
        print("\n")

print(f"Total time taken for all passwords: {total_time:.4f} ms")
print(f"Average time taken per password: {total_time / 100:.4f} ms")
