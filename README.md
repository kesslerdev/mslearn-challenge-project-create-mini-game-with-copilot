# Rock, Paper, Scissors - Python CLI Game

A simple command-line implementation of the classic Rock, Paper, Scissors game built with Python.

## Project Overview

This project implements a console-based Rock, Paper, Scissors game where a player competes against the computer. The game features score tracking, input validation, and a clean command-line interface.

## Game Specification

### Rules
- **Rock** beats **Scissors** (rock crushes scissors)
- **Scissors** beats **Paper** (scissors cuts paper)
- **Paper** beats **Rock** (paper covers rock)
- Identical choices result in a **tie**

### Features

#### Core Functionality
- Single player vs computer gameplay
- Random computer move generation
- Real-time score tracking (wins, losses, ties)
- Input validation with error handling
- Multiple rounds support
- Clean game exit option
- **Color-coded output for enhanced visual experience**

#### User Interface
- Welcome message with game instructions
- Clear prompts for user input
- Formatted display of each round's results
- Running score display
- Game summary on exit
- **Color-coded messages:**
  - Green for wins
  - Red for losses
  - Yellow for ties
  - Blue for information
  - Cyan for player/computer choices
  - Magenta for scores

### Technical Requirements

#### Python Implementation
- Python 3.6 or higher
- Use of `random` module for computer moves
- Input validation using `input()` function
- Proper exception handling
- Clean code structure with functions

#### Game Flow
1. Display welcome message and rules
2. Enter main game loop:
   - Prompt user for choice (rock/paper/scissors/quit)
   - Validate user input
   - Generate computer choice
   - Determine round winner
   - Display results
   - Update and show score
   - Continue until user quits
3. Display final statistics
4. Thank user and exit

#### Input Handling
- Accept multiple input formats:
  - Full words: "rock", "paper", "scissors"
  - Single letters: "r", "p", "s"
  - Case insensitive
- Special commands:
  - "quit", "q", "exit" to end game
  - "help", "rules" to display rules
- Invalid input handling with re-prompt

#### Output Format
```
=== ROCK, PAPER, SCISSORS ===

Enter your choice (rock/paper/scissors) or 'quit' to exit: rock
You chose: Rock
Computer chose: Scissors
You win! Rock crushes Scissors.

Score - You: 1 | Computer: 0 | Ties: 0
```
*Note: Actual output includes color coding for better visual distinction*

### File Structure
```
/
├── README.md
├── app.py           # Main game file
└── requirements.txt # Python dependencies (if any)
```

### Implementation Guidelines

#### Required Functions
- `get_user_choice()` - Handle user input and validation
- `get_computer_choice()` - Generate random computer move
- `determine_winner(user_choice, computer_choice)` - Game logic
- `display_result(user_choice, computer_choice, result)` - Format output
- `play_game()` - Main game loop
- `main()` - Entry point

#### Code Quality Standards
- Use descriptive variable and function names
- Include docstrings for functions
- Handle edge cases and errors gracefully
- Follow PEP 8 style guidelines
- Keep functions focused and modular

### User Stories

**As a player, I want to:**
- Start the game with a simple command
- Choose my move using intuitive input
- See what the computer chose
- Know immediately who won each round
- Track my performance across multiple rounds
- Quit the game whenever I want
- See my final score when I finish

**As a developer, I want to:**
- Write clean, readable Python code
- Implement proper error handling
- Create reusable functions
- Follow Python best practices
- Make the code easy to test and maintain

### Getting Started

#### Prerequisites
- Python 3.6 or higher installed
- Basic command line knowledge

#### Running the Game
```bash
# Run the game
python app.py
```

#### Example Gameplay
```
Welcome to Rock, Paper, Scissors!

Rules:
- Rock beats Scissors
- Scissors beats Paper  
- Paper beats Rock

Enter your choice (rock/paper/scissors) or 'quit' to exit: rock
You chose: Rock
Computer chose: Paper
You lose! Paper covers Rock.

Score - You: 0 | Computer: 1 | Ties: 0

Enter your choice (rock/paper/scissors) or 'quit' to exit: quit

Final Score:
You: 0 wins
Computer: 1 wins
Ties: 0

Thanks for playing!
```

### Future Enhancements
- Best of N rounds mode
- Difficulty levels
- Game statistics persistence
- ~~Color-coded output~~ ✅ **Implemented**
- ASCII art for choices
- Tournament mode

### Testing
Consider testing these scenarios:
- Valid inputs (rock, paper, scissors, r, p, s)
- Invalid inputs
- Case sensitivity
- Quit commands
- Score tracking accuracy
- Computer randomness

This specification provides a complete foundation for building a professional Rock, Paper, Scissors CLI game in Python.