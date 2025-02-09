# Python script to check the strength of the password.

# Reusable Function to check if the password has at least 8 characters
def has_min_length(password):
    # Returns True if password length is 8 or more
    return len(password) >= 8

# Reusable Function to check if the password contains both uppercase and lowercase letters
def has_upper_and_lower(password):
    # Returns True if at least one uppercase and one lowercase letter are found
    return any(c.isupper() for c in password) and any(c.islower() for c in password)
    
# Reusable Function to check if the password contains at least one numeric digit
def has_digit(password):
    # Returns True if at least one digit (0-9) is found
    return any(c.isdigit() for c in password)

# Function to check if the password contains at least one special character
def has_special_char(password):
    # Set of allowed special characters
    special_chars = set("!@#$%^&*(),.?\":{}|<>")
    # Returns True if at least one special character is found
    return any(c in special_chars for c in password)

# Function to check password strength based on multiple criteria
def check_password_strength(password):
    # Dictionary storing each password strength rule and its corresponding check result (True/False)
    criteria_checks = {
        "The password should be at least 8 characters long.": has_min_length(password),
        "The password should contain both uppercase and lowercase letters.": has_upper_and_lower(password),
        "The password should contain at least one digit (0-9).": has_digit(password),
        "The password should contain at least one special character (e.g., !, @, #, $, %).": has_special_char(password),
    }

    # Count how many criteria are met
    passed_criteria_count = sum(criteria_checks.values())  
    # Total number of criteria
    total_criteria = len(criteria_checks)

    # Case 1: If no criteria are met, password is very weak
    if passed_criteria_count == 0:
        print("Password is Weak!")
        for msg in criteria_checks.keys():
            print(f"- {msg}")
        return False

    # Case 2: If all criteria are met, password is strong
    if passed_criteria_count == total_criteria:
        print("Password is Strong!")
        return True

    # Case 3: Password meets some but not all criteria
    strength_percentage = (passed_criteria_count / total_criteria) * 100
    print(f"Password is {int(strength_percentage)}% Strong!")

    # Print only FAILED criteria
    for msg, passed in criteria_checks.items():
        if not passed:
            print(f"- {msg}")

    # Return False to indicate a weak password
    return False

# Prompt user for password input and store in variable
password = input("Enter your password: ")

# Call the function to check password strength
check_password_strength(password)
