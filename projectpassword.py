import random
import string

CHAR_GROUPS = (string.ascii_letters, string.digits, string.punctuation)
saved_passwords = {}

def generate_password_recursive(length, chars):
    """
    >>> generate_password_recursive(0, "a")
    ''
    """
    if length <= 0:
        return ""
    return random.choice(chars) + generate_password_recursive(length - 1, chars)


# Topic: Nested Loops (outer loop over passwords, inner loop builds characters)
def generate_batch_nested(count, length, chars):
    passwords = []
    for _ in range(count):  # Outer loop over passwords
        pwd = ""
        for _ in range(length):  # Inner loop over characters
            pwd += random.choice(chars)
        passwords.append(pwd)
    return passwords

def check_strength(password):
    """
    >>> check_strength("abc")[0]
    'Weak'
    """
    score = 0
    types_found = set() 

    for char in password:
        if char in CHAR_GROUPS[0]:
            types_found.add("letter")
        elif char in CHAR_GROUPS[1]:
            types_found.add("digit")
        elif char in CHAR_GROUPS[2]:
            types_found.add("symbol")

    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    else:
        score += 1

    score += len(types_found)

    if score >= 5:
        return "Strong", score
    elif score >= 3:
        return "Medium", score
    else:
        return "Weak", score

# Safe Input Handling
def safe_int_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Enter a valid integer.")

def safe_bool_input(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'yes']:
            return True
        if choice in ['n', 'no']:
            return False
        print("Invalid input! Enter 'y' or 'n'.")

# File Handling & Dictionary Update
def save_password(site, password):
    saved_passwords[site] = password  # Update dictionary
    try:
        with open("passwords.txt", "a") as file:
            file.write(f"Site: {site} | Password: {password}\n")
        print(f"Saved password for {site} successfully!")
    except IOError as e:
        print(f"File error: {e}")

def main():
    while True:
        print("\n--- Password Generator & Checker ---")
        print("1. Generate Passwords")
        print("2. Check Password Strength")
        print("3. View Saved Passwords")
        print("4. Exit\n")
        
        if choice == "1":
            length = safe_int_input("Enter password length: ")
            use_digits = safe_bool_input("Include digits? (y/n): ")
            use_symbols = safe_bool_input("Include symbols? (y/n): ")
            count = safe_int_input("How many passwords to generate?: ")

            # Build allowed characters
            allowed = CHAR_GROUPS[0]
            if use_digits:
                allowed += CHAR_GROUPS[1]
            if use_symbols:
                allowed += CHAR_GROUPS[2]
                
            # Generate multiple passwords using recursion
            passwords = [generate_password_recursive(length, allowed) for _ in range(count)]

            print("\nGenerated Passwords:")
            for idx, pwd in enumerate(passwords, start=1):
                strength, score = check_strength(pwd)
                print(f"{idx}. {pwd} (Strength: {strength}, Score: {score})")

            if safe_bool_input("\nSave one of these passwords? (y/n): "):
                while True:
                    sel = safe_int_input(f"Select password number (1-{count}): ")
                    if 1 <= sel <= count:
                        chosen = passwords[sel - 1]
                        break
                    print("Number out of range.")

                site = input("Enter site name: ").strip()
                if site:
                    save_password(site, chosen)
                    
        elif choice == "2":
            pwd = input("Enter password to rate: ")
            strength, score = check_strength(pwd)
            print(f"Strength: {strength} (Score: {score})")
            print()

        elif choice == "3":
            print("\nSaved Passwords :")
            for site, pwd in saved_passwords.items():
                print(f"{site}: {pwd}")
            print() 

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")





