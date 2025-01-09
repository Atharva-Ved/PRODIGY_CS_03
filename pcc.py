import re

def check_password_strength(password):
    # Initialize the feedback list
    feedback = []
    strength = 0
    
    # Check if the password length is at least 8 characters
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check if the password contains at least one uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check if the password contains at least one lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check if the password contains at least one digit
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")
    
    # Check if the password contains at least one special character
    if re.search(r'[@#$%^&+=!]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (@, #, $, %, ^, &, +, =, !).")
    
    # Provide the final password strength
    if strength == 5:
        feedback.insert(0, "Strong password!")
    elif strength == 4:
        feedback.insert(0, "Moderately strong password.")
    elif strength == 3:
        feedback.insert(0, "Weak password.")
    else:
        feedback.insert(0, "Very weak password.")
    
    return feedback

def main():
    while True:
        # Prompt user for password input
        password = input("Enter a password to check its strength: ")

        # Call function to evaluate the password
        feedback = check_password_strength(password)

        # Print the feedback
        for message in feedback:
            print(message)

        # If the password is strong, break the loop
        if "Strong password!" in feedback[0]:
            print("\nYour password meets all the requirements!")
            break
        else:
            print("\nPlease try again with a stronger password.\n")

if __name__ == "__main__":
    main()
