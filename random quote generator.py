import os
import random

# Function to load quotes from a file
def load_file(filename):
    try:
        with open(filename, 'r') as file:
            quotes = file.readlines()
            return [quote.strip() for quote in quotes]
    except FileNotFoundError:
        print(f"{filename} does not exist.")
        return []

# Function to create a default file with sample quotes
def default_file(filename):
    default_quotes = [
        "If you're brave enough to say goodbye, life will reward you with a new hello.",
        "The best way to predict your future is to create it.",
        "Act as if what you do makes a difference. It does."
    ]

    with open(filename, 'w') as file:
        for quote in default_quotes:
            file.write(quote + "\n")
    print(f"Default file '{filename}' has been created with sample quotes.")

# Function to select a random quote from a list
def random_quote(quotes):
    return random.choice(quotes) if quotes else "No quotes available."

# Main function to ask user if they have a file or create one
def main():
    user_input = input("Do you have a quotes file? (Y/N): ").strip().upper()

    if user_input == "Y":
        filename = input("Please enter the file path or press Enter for 'quotes.txt': ").strip()
        filename = filename if filename else "quotes.txt"
    else:
        filename = "quotes.txt"
        if not os.path.exists(filename):
            default_file(filename)

    # Load the quotes and display a random one
    quotes = load_file(filename)
    print("\nHere's a random quote for you:")
    print(random_quote(quotes))

if __name__ == "__main__":
    main()
