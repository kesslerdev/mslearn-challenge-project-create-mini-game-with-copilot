import random

class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    BLUE_BOLD = BLUE + BOLD
    RED_BOLD = RED + BOLD
    CYAN_BOLD = CYAN + BOLD
    GREEN_BOLD = GREEN + BOLD
    YELLOW_BOLD = YELLOW + BOLD
    MAGENTA_BOLD = MAGENTA + BOLD
    WHITE_BOLD = WHITE + BOLD
    
    @staticmethod
    def colorize(text, color):
        """Apply color to text"""
        return f"{color}{text}{Colors.RESET}"

def get_user_choice():
    """
    Get and validate user input for their choice.
    Returns normalized choice or None for quit commands.
    """
    while True:
        choice = input(Colors.colorize("Enter your choice (rock/paper/scissors) or 'quit' to exit: ", Colors.WHITE)).lower().strip()
        
        # Handle quit commands
        if choice in ['quit', 'q', 'exit']:
            return None
            
        # Handle help commands
        if choice in ['help', 'rules']:
            print(Colors.colorize("\nRules:", Colors.BLUE_BOLD))
            print(Colors.colorize("- Rock beats Scissors", Colors.BLUE))
            print(Colors.colorize("- Scissors beats Paper", Colors.BLUE))
            print(Colors.colorize("- Paper beats Rock\n", Colors.BLUE))
            continue
            
        # Handle valid choices
        if choice in ['rock', 'r']:
            return 'rock'
        elif choice in ['paper', 'p']:
            return 'paper'
        elif choice in ['scissors', 's']:
            return 'scissors'
        else:
            print(Colors.colorize("Invalid choice! Please enter rock, paper, scissors, or quit.", Colors.RED))

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
    print(f"\n{Colors.colorize('You chose:', Colors.CYAN)} {Colors.colorize(user_choice.capitalize(), Colors.CYAN_BOLD)}")
    print(f"{Colors.colorize('Computer chose:', Colors.CYAN)} {Colors.colorize(computer_choice.capitalize(), Colors.CYAN_BOLD)}")

    if result == 'tie':
        print(Colors.colorize("It's a tie!", Colors.YELLOW_BOLD))
    elif result == 'user':
        # Display winning message based on choices
        messages = {
            ('rock', 'scissors'): "You win! Rock crushes Scissors.",
            ('scissors', 'paper'): "You win! Scissors cuts Paper.",
            ('paper', 'rock'): "You win! Paper covers Rock."
        }
        print(Colors.colorize(messages[(user_choice, computer_choice)], Colors.GREEN_BOLD))
    else:
        # Display losing message based on choices
        messages = {
            ('scissors', 'rock'): "You lose! Rock crushes Scissors.",
            ('paper', 'scissors'): "You lose! Scissors cuts Paper.",
            ('rock', 'paper'): "You lose! Paper covers Rock."
        }
        print(Colors.colorize(messages[(user_choice, computer_choice)], Colors.RED_BOLD))

def play_game():
    """
    Main game loop that handles the gameplay flow.
    """
    print(Colors.colorize("=== ROCK, PAPER, SCISSORS ===", Colors.MAGENTA_BOLD))
    print(Colors.colorize("\nWelcome to Rock, Paper, Scissors!", Colors.BLUE_BOLD))
    print(Colors.colorize("\nRules:", Colors.BLUE_BOLD))
    print(Colors.colorize("- Rock beats Scissors", Colors.BLUE))
    print(Colors.colorize("- Scissors beats Paper", Colors.BLUE))
    print(Colors.colorize("- Paper beats Rock", Colors.BLUE))
    print(Colors.colorize("\nYou can also type 'help' for rules or 'quit' to exit.\n", Colors.WHITE))
    
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
        score_text = f"Score - You: {user_wins} | Computer: {computer_wins} | Ties: {ties}"
        print(f"\n{Colors.colorize(score_text, Colors.MAGENTA_BOLD)}")
        print(Colors.colorize("-" * 50, Colors.WHITE))
    
    # Display final statistics
    print(Colors.colorize(f"\nFinal Score:", Colors.BLUE_BOLD))
    print(Colors.colorize(f"You: {user_wins} wins", Colors.GREEN))
    print(Colors.colorize(f"Computer: {computer_wins} wins", Colors.RED))
    print(Colors.colorize(f"Ties: {ties}", Colors.YELLOW))
    print(Colors.colorize(f"Total games played: {user_wins + computer_wins + ties}", Colors.WHITE))
    
    if user_wins > computer_wins:
        print(Colors.colorize("Congratulations! You won overall!", Colors.GREEN_BOLD))
    elif computer_wins > user_wins:
        print(Colors.colorize("Computer wins overall! Better luck next time!", Colors.RED_BOLD))
    else:
        print(Colors.colorize("It's a tie overall! Great game!", Colors.YELLOW_BOLD))
    
    print(Colors.colorize("\nThanks for playing!", Colors.BLUE_BOLD))

def main():
    """
    Entry point of the program.
    """
    try:
        play_game()
    except KeyboardInterrupt:
        print(Colors.colorize("\n\nGame interrupted. Thanks for playing!", Colors.YELLOW))
    except Exception as e:
        print(Colors.colorize(f"\nAn error occurred: {e}", Colors.RED))
        print(Colors.colorize("Thanks for playing!", Colors.BLUE))

if __name__ == "__main__":
    main()