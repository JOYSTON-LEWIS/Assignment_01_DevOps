# Python script to check the strength of the password.

# Prompt the user to enter a password
password = input("Enter your password: ")

# Function to check the strength of the password based on predefined criteria
def check_password_strength(password):
    # Counting Number Of True Cases to denote how strong the password is
    passed_criteria_count = 0
    total_criteria = 4

    # Preparing Reusable Variables to check if the password meets different strength criteria

    # Criteria One: Checks if password has at least 8 characters
    criteria_one = contains_eight_characters_or_more(password)

    # Criteria Two: Checks if password contains both uppercase and lowercase letters
    criteria_two = contains_upper_and_lower(password)
    
    # Criteria Three: Checks if password contains at least one digit
    criteria_three = contains_digit(password)
    
    # Criteria Four: Checks if password contains at least one special character
    criteria_four = contains_special_character(password)

    # If all criteria are met, the password is considered strong
    if criteria_one and criteria_two and criteria_three and criteria_four:
        # Inform the user
        print('Password Strength is 100% Strong!')
        # Return True to indicate a strong password
        return True
    else:
        # Checking criteria one failure and returning appropriate error message to user
        if not criteria_one:
            print('The password should be at least 8 characters long.')
        # If criteria one is success incrementing passed_criteria_count for calculation of password strength in percentage
        elif criteria_one:
            passed_criteria_count += 1

        # Checking criteria two failure and returning appropriate error message to user
        if not criteria_two:
            print('The password should contain both uppercase and lowercase letters.')
        # If criteria two is success incrementing passed_criteria_count for calculation of password strength in percentage
        elif criteria_two:
            passed_criteria_count += 1

        # Checking criteria three failure and returning appropriate error message to user
        if not criteria_three:
            print('The password should contain at least one digit (0-9).')
        # If criteria three is success incrementing passed_criteria_count for calculation of password strength in percentage
        elif criteria_three:
            passed_criteria_count += 1

        # Checking criteria four failure and returning appropriate error message to user
        if not criteria_four:
            print('The password should contain at least one special character (e.g., !, @, #, $, %).')
        # If criteria four is success incrementing passed_criteria_count for calculation of password strength in percentage
        elif criteria_four:
            passed_criteria_count += 1

        # Calling Function to get how strong password is in percentage
        number_of_criteria_cleared(passed_criteria_count, total_criteria)
        # Return False to indicate a weak password
        return False

# Function to check if the password has at least 8 characters
def contains_eight_characters_or_more(password):
    # Returns True if length is 8 or more, otherwise False
    return len(password) > 7

# Function to check if the password contains both uppercase and lowercase letters
def contains_upper_and_lower(password):
    # Returns True if both uppercase and lowercase letters are found, otherwise False
    return any(c.isupper() for c in password) and any(c.islower() for c in password)

# Function to check if the password contains at least one numeric digit
def contains_digit(password):
    # Returns True if atleast one numeric digit is found, otherwise False
    return any(char.isdigit() for char in password)

# Function to check if the password contains at least one special character
def contains_special_character(password):
    # Set of special characters to check against
    special_chars = set("!@#$%^&*(),.?\":{}|<>")
    # Returns True if atleast one special character is found, otherwise False
    return any(char in special_chars for char in password)

# Function to get how strong the password is in percentage
def number_of_criteria_cleared(actual, total):
    # Check if both inputs are integers
    if not isinstance(actual, int) or not isinstance(total, int):
        # Simply Exiting The Function because within program exceptions need not be shown to the user
        return
    
    # Check if total is zero to prevent division by zero
    if total <= 0:
        # Simply Exiting The Function because within program exceptions need not be shown to the user
        return
    
    # Check if total is zero to prevent division by zero
    if actual < 0:
        # Simply Exiting The Function because within program exceptions need not be shown to the user
        return
    
    # Checking if none or some of the criteria are passed and informing the user
    if(actual == 0):
        # Printing Strength of Password to the User
        print(f"Your Password is Weak!")
    else:
        # Printing Strength of Password to the User
        print(f"Your Password is only {int(actual * 100 / total)}% Strong!")
    # Exiting from the function
    return

# Call the function to check the entered password's strength
check_password_strength(password)
