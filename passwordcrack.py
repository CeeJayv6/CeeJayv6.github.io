import itertools
import string
import time

# Brute Force Password Cracking
def brute_force_crack(target_password):
    characters = string.ascii_lowercase + string.digits  # Only lowercase letters and digits for speed
    start_time = time.time()  # Track time taken for cracking

    for length in range(1, len(target_password) + 1):  # Limit to password length
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            print(f"Trying: {guess_password}")  # Debugging output
            if guess_password == target_password:
                end_time = time.time()
                print(f"Password cracked! The password is: {guess_password}")
                print(f"Time taken: {end_time - start_time} seconds")
                return guess_password
    print("Password not found within the given character set.")
    return None

# Dictionary-based Password Cracking
def dictionary_crack(target_password, wordlist):
    try:
        with open(wordlist, 'r') as file:
            for word in file:
                guess_password = word.strip()  # Remove any extra newline/space
                print(f"Trying: {guess_password}")  # Debugging output
                if guess_password == target_password:
                    print(f"Password cracked! The password is: {guess_password}")
                    return guess_password
    except FileNotFoundError:
        print(f"Error: The file {wordlist} was not found.")
    print("Password not found in the dictionary.")
    return None

# Main function to choose cracking method
def main():
    print("Welcome to the Python Password Cracking Tool!")
    
    # Get the method choice from the user
    method = input("Choose cracking method (1 for Brute Force, 2 for Dictionary): ").strip()

    target_password = input("Enter the target password: ").strip()  # The password to crack

    if method == '1':
        print("\nUsing Brute Force Method...")
        brute_force_crack(target_password)
    elif method == '2':
        print("\nUsing Dictionary Method...")
        wordlist = input("Enter the path to your wordlist file (e.g., 'wordlist.txt'): ").strip()
        dictionary_crack(target_password, wordlist)
    else:
        print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
