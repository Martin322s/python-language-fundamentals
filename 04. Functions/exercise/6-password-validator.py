def validate_password(password):
    valid = True

    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        valid = False

    if not password.isalnum():
        print("Password must consist only of letters and digits")
        valid = False

    digit_count = sum(1 for ch in password if ch.isdigit())
    if digit_count < 2:
        print("Password must have at least 2 digits")
        valid = False

    if valid:
        print("Password is valid")


pwd = input()
validate_password(pwd)