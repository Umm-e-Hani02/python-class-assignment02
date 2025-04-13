import random # Import random module to generate random numbers

def generate_secret_number():
    """
    Generates a random 3-digit secret number with unique digits.
    Returns:
        str: A 3-digit number as a string
    """
    digits = list("0123456789")  # Create a list of all possible digits
    random.shuffle(digits)        # Randomly shuffle the digits
    return ''.join(digits[:3])    # Take first 3 digits and join them into a string

def give_feedback(secret, guess):
    """
    Provides feedback for each digit in the guess compared to the secret number.
    👌 - Correct digit in correct position
    👍 - Correct digit in wrong position
    ❌ - Digit not in secret number
    
    Args:
        secret (str): The secret number
        guess (str): The player's guess
    Returns:
        str: Feedback string with emojis
    """
    feedback = []
    for i in range(3):
        if guess[i] == secret[i]:
            feedback.append("👌")  # Digit is correct and in right position
        elif guess[i] in secret:
            feedback.append("👍")  # Digit is correct but in wrong position
        else:
            feedback.append("❌")  # Digit is not in secret number
    return ''.join(feedback)

def main():
    """
    Main game loop that handles:
    - Game initialization
    - Player input
    - Feedback display
    - Win/lose conditions
    - Attempt tracking
    """
    print("\n🎯 Welcome to number guessing game!")

    secret = generate_secret_number()  # Generate the secret number
    attempts = 10                      # Set number of attempts
    
    while attempts > 0:
        # Get player's guess
        guess = input("Enter 3 digits number: ")
        
        # Validate input
        if len(guess) != 3 or not guess.isdigit():
            print("⚠️Please enter a valid 3-digit number.")
            continue

        # Get and display feedback
        feedback = give_feedback(secret, guess)
        print(feedback)
            
        # Check for win condition
        if feedback == "👌👌👌":
            print("🎉 You Got IT! 🎉")
            break

        # Update attempts and display remaining
        attempts -= 1
        print(f"Attempts left: {attempts}")

    else:  # This block executes when while loop ends without break
        print(f"Game Over! The secret number was: {secret}")

# Entry point of the program
if __name__ == "__main__":
    main()
