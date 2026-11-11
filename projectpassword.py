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
