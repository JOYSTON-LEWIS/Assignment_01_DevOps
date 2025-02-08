# Python script to check the strength of the password.

# Prompt the user to enter a password
password = input("Enter your password: ")

# Function to check the strength of the password based on predefined criteria
def check_password_strength(password):
    # Check if the password meets different strength criteria
    criteria_one = contains_eight_characters_or_more(password)  # Checks if password has at least 8 characters
    criteria_two = contains_upper_and_lower(password)  # Checks if password contains both uppercase and lowercase letters
    criteria_three = contains_digit(password)  # Checks if password contains at least one digit
    criteria_four = contains_special_character(password)  # Checks if password contains at least one special character

    # If all criteria are met, the password is considered strong
    if criteria_one and criteria_two and criteria_three and criteria_four:
        print(True)  # Indicates password meets all criteria
        print('Password Meets The Given Criteria')  # Inform the user
        return True  # Return True to indicate a strong password
    else:
        # If any criteria are not met, print False and provide feedback
        print(False)
        if not criteria_one:
            print('The password should be at least 8 characters long.')
        if not criteria_two:
            print('The password should contain both uppercase and lowercase letters.')
        if not criteria_three:
            print('The password should contain at least one digit (0-9).')
        if not criteria_four:
            print('The password should contain at least one special character (e.g., !, @, #, $, %).')
        return False  # Return False to indicate a weak password

# Function to check if the password has at least 8 characters
def contains_eight_characters_or_more(password):
    return len(password) > 7  # Returns True if length is 8 or more, otherwise False

# Function to check if the password contains both uppercase and lowercase letters
def contains_upper_and_lower(password):
    return any(c.isupper() for c in password) and any(c.islower() for c in password)

# Function to check if the password contains at least one numeric digit
def contains_digit(password):
    return any(char.isdigit() for char in password)

# Function to check if the password contains at least one special character
def contains_special_character(password):
    special_chars = set("!@#$%^&*(),.?\":{}|<>")  # Set of special characters to check against
    return any(char in special_chars for char in password)

# Call the function to check the entered password's strength
check_password_strength(password)