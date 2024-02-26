import re

def validate_password(username, password):
    # Compile regex for forbidden words and username
    forbidden_regex = re.compile(r'facebook|amazon|ebay|instagram', re.IGNORECASE)
    username_regex = re.compile(re.escape(username), re.IGNORECASE)  # Use re.escape to handle special characters in username
    
    # Check for the presence of forbidden words
    if forbidden_regex.search(password):
        return False
    
    # Check if the username is part of the password
    if username_regex.search(password):
        return False
    
    # Add more password checks here as needed (e.g., length, complexity)
    
    return True

def main():
    username = input("Enter a username: ")
    
    while True:
        password1 = input("Enter your password: ")
        password2 = input("Re-enter your password: ")
        
        if password1 != password2:
            print("Passwords do not match. Please try again.")
            continue
        
        if not validate_password(username, password1):
            print("Invalid password. Make sure your password does not include your username or forbidden words (Facebook, Amazon, Ebay, Instagram).")
            continue
        
        print("Username and password have been set successfully!")
        break

if __name__ == "__main__":
    main()
