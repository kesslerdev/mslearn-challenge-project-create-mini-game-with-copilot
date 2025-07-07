import random

def get_user_choice():
    """
    Get and validate user input for their choice.
    Returns normalized choice or None for quit commands.
    """
    while True:
        choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()
        
        # Handle quit commands
        if choice in ['quit', 'q', 'exit']:
            return None
            
        # Handle help commands
        if choice in ['help', 'rules']:
            print("\nRules:")
            print("- Rock beats Scissors")
            print("- Scissors beats Paper")
            print("- Paper beats Rock\n")
            continue
            
        # Handle valid choices
        if choice in ['rock', 'r']:
            return 'rock'
        elif choice in ['paper', 'p']:
            return 'paper'
        elif choice in ['scissors', 's']:
            return 'scissors'
        else:
            print("Invalid choice! Please enter rock, paper, scissors, or quit.")

def get_computer_choice():
    """
    Generate a random choice for the computer.
    Returns one of: 'rock', 'paper', 'scissors'
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of a round.
    Returns 'user', 'computer', or 'tie'
    """
    if user_choice == computer_choice:
        return 'tie'
    
    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, result):
    """
    Display the result of a round with formatted output.
    """
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        # Display winning message based on choices
        messages = {
            ('rock', 'scissors'): "You win! Rock crushes Scissors.",
            ('scissors', 'paper'): "You win! Scissors cuts Paper.",
            ('paper', 'rock'): "You win! Paper covers Rock."
        }
        print(messages[(user_choice, computer_choice)])
    else:
        # Display losing message based on choices
        messages = {
            ('scissors', 'rock'): "You lose! Rock crushes Scissors.",
            ('paper', 'scissors'): "You lose! Scissors cuts Paper.",
            ('rock', 'paper'): "You lose! Paper covers Rock."
        }
        print(messages[(user_choice, computer_choice)])

def play_game():
    """
    Main game loop that handles the gameplay flow.
    """
    print("=== ROCK, PAPER, SCISSORS ===")
    print("\nWelcome to Rock, Paper, Scissors!")
    print("\nRules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    print("\nYou can also type 'help' for rules or 'quit' to exit.\n")
    
    # Initialize score tracking
    user_wins = 0
    computer_wins = 0
    ties = 0
    
    while True:
        # Get user choice
        user_choice = get_user_choice()
        
        # Check if user wants to quit
        if user_choice is None:
            break
            
        # Get computer choice
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        
        # Display round result
        display_result(user_choice, computer_choice, result)
        
        # Update score
        if result == 'user':
            user_wins += 1
        elif result == 'computer':
            computer_wins += 1
        else:
            ties += 1
            
        # Display current score
        print(f"\nScore - You: {user_wins} | Computer: {computer_wins} | Ties: {ties}")
        print("-" * 50)
    
    # Display final statistics
    print(f"\nFinal Score:")
    print(f"You: {user_wins} wins")
    print(f"Computer: {computer_wins} wins")
    print(f"Ties: {ties}")
    print(f"Total games played: {user_wins + computer_wins + ties}")
    
    if user_wins > computer_wins:
        print("Congratulations! You won overall!")
    elif computer_wins > user_wins:
        print("Computer wins overall! Better luck next time!")
    else:
        print("It's a tie overall! Great game!")
    
    print("\nThanks for playing!")

def main():
    """
    Entry point of the program.
    """
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Thanks for playing!")

if __name__ == "__main__":
    main()