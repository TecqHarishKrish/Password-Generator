import random
import string
import pyfiglet
import os
import time

def generate_password(length=12, include_words=False, num_words=2):
    """Generate a strong and customizable password."""
    if length < 8:
        raise ValueError("Password length must be at least 8 for strong security.")

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure password includes at least one character from each pool
    all_chars = lowercase + uppercase + digits + special_chars
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    # Include word-like patterns if required
    if include_words:
        random_words = ''.join(random.choices(lowercase, k=num_words * 4))
        password.insert(random.randint(0, len(password)), random_words)

    return ''.join(password)

def password_strength(password):
    """Evaluate password strength based on length and character diversity."""
    length = len(password)
    unique_chars = len(set(password))
    
    if length >= 16 and unique_chars > 10:
        return "Very Strong 💎"
    elif length >= 12 and unique_chars > 8:
        return "Strong 💪"
    elif length >= 10 and unique_chars > 6:
        return "Moderate 👍"
    else:
        return "Weak 😟"

def save_password_to_file(password):
    """Save the password to a text file."""
    file_path = "generated_password.txt"
    with open(file_path, "a") as file:
        file.write(f"{password}\n")
    print(f"\033[1;34mPassword saved to '{file_path}'! ✔\033[0m")

def display_banner(message):
    """Display an ASCII art banner."""
    banner = pyfiglet.figlet_format(message, font="slant")
    print(f"\033[1;32m{banner}\033[0m")

def progress_bar(duration=2):
    """Display a loading progress bar for effect."""
    print("\033[1;33mGenerating your password...\033[0m", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(duration / 3)
    print("\033[1;32m Done!\033[0m\n")

def main():
    display_banner("Password Generator")
    
    # Input options from the user
    print("\033[1;36mWelcome to the Ultimate Password Generator! 🚀\033[0m")
    print("1. Generate a strong password")
    print("2. Generate a memorable password (with random words)")
    choice = input("\033[1;33mChoose an option (1 or 2, default is 1): \033[0m").strip() or "1"
    
    # Password length
    length = input("\033[1;33mEnter the desired password length (default is 12): \033[0m").strip()
    password_length = int(length) if length.isdigit() else 12

    # Generate password based on choice
    if choice == "1":
        password = generate_password(length=password_length)
    elif choice == "2":
        num_words = input("\033[1;33mHow many word-like patterns to include? (default is 2): \033[0m").strip()
        word_count = int(num_words) if num_words.isdigit() else 2
        password = generate_password(length=password_length, include_words=True, num_words=word_count)
    else:
        print("\033[1;31mInvalid choice! Defaulting to strong password generation.\033[0m")
        password = generate_password(length=password_length)
    
    # Show progress bar
    progress_bar()

    # Display password
    print("\033[1;33mGenerated Password:\033[0m \033[1;35m{}\033[0m".format(password))
    print("\033[1;33mPassword Strength:\033[0m", password_strength(password))
    
    # Save or regenerate
    while True:
        print("\n\033[1;36mOptions:\033[0m")
        print("1. Save password to a file")
        print("2. Regenerate a new password")
        print("3. Exit")
        action = input("\033[1;33mChoose an option: \033[0m").strip()
        if action == "1":
            save_password_to_file(password)
        elif action == "2":
            print("\033[1;32mRegenerating a new password...\033[0m")
            password = generate_password(length=password_length)
            print("\n\033[1;33mNew Password:\033[0m \033[1;35m{}\033[0m".format(password))
            print("\033[1;33mPassword Strength:\033[0m", password_strength(password))
        elif action == "3":
            print("\033[1;34mThank you for using the Password Generator! Stay secure! 🚀\033[0m")
            break
        else:
            print("\033[1;31mInvalid choice! Please try again.\033[0m")

if __name__ == "__main__":
    main()
