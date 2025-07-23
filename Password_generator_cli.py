import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generates a password based on user-defined criteria."""
    
    # Define the character sets
    letters = string.ascii_letters  # Contains uppercase and lowercase letters
    numbers = string.digits
    symbols = string.punctuation
    
    # Create the pool of characters to choose from
    char_pool = ""
    if use_letters:
        char_pool += letters
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols
        
    if not char_pool:
        print("Error: You must select at least one character type.")
        return None
        
    # Generate the password
    try:
        password = ''.join(random.choice(char_pool) for _ in range(length))
        return password
    except IndexError:
        print("Error: Cannot generate password from an empty character pool.")
        return None


def main():
    """Main function to run the password generator CLI."""
    print("--- 🐍 Python Password Generator ---")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 12): "))
            if length > 0:
                break
            else:
                print("Please enter a positive number for the length.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    # Get user preferences for character types
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    # Generate and display the password
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    
    if password:
        print("\n✨ Generated Password ✨")
        print(f"Your new password is: {password}")

    # --- FIX ---
    # This line will pause the script and wait for user input before closing.
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
