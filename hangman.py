import random
from words import word_list  


def get_word():
    word = random.choice(word_list)  
    return word.upper()  

# Function to handle the gameplay
def play(word):
    word_completion = "_" * len(word)  # This represents the guessed word, starting with all blanks
    guessed = False  # To track if the player has guessed the word
    guessed_letters = []  # List to store the letters the player has guessed
    guessed_words = []  # List to store the full word guesses the player has made
    tries = 6  # Number of tries the player has to guess the word
    
    print("Let's play Hangman!")
    print(display_hangman(tries))  
    print(word_completion) 
    print("\n")
    
  

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()  
        if len(guess) == 1 and guess.isalpha():  # If input is a single letter

            if guess in guessed_letters:  
                print(f"You already guessed the letter {guess}")

            elif guess not in word:  # If the letter is not in the word
                print(f"{guess} is not in the word.")
                tries -= 1  # Reduce the number of tries
                guessed_letters.append(guess)  # Add the guess to the guessed_letters list

            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)  
                word_as_list = list(word_completion)  # Convert the word_completion string to a list
                indices = [i for i, letter in enumerate(word) if letter == guess]  # Find where the guessed letter appears in the word
                for index in indices:
                    word_as_list[index] = guess  # Update the guessed letters in the list
                word_completion = "".join(word_as_list)  # Join the list back into a string
                if "_" not in word_completion:
                    guessed = True  # Set guessed to True if there are no blanks left
                    
        elif len(guess) == len(word) and guess.isalpha():  # If input is a word guess
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word  # The player guessed the correct word
        else:
            print("Not a valid guess.")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print(f"Congrats, you guessed the word {word}!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Better luck next time!")

# Function to display the hangman figure based on the number of tries left
def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,  # Final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,  # Head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,  # Head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |      
           -
        """,  # Head, torso, and one arm
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
           -
        """,  # Head and torso
        """
           --------
           |      |
           |      O
           |    
           |      
           |      
           -
        """,  # Head only
        """
           --------
           |      |
           |      
           |    
           |      
           |      
           -
        """  # Initial empty state
    ]
    return stages[tries]

# Main logic to start the game
def main():
    word = get_word()  # Get a random word
    play(word)  # Start the game

if __name__ == "__main__":
    main()
