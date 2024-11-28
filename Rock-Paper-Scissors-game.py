import random

choices = ['rock', 'paper', 'scissors']
def get_user_choice():
    """Prompt the user for their choice and validate it."""
    while True:
        user_input = input("Enter your choice (rock, paper, scissors or 'quit' to exit): ").lower()
        if user_input in choices or user_input == 'quit':
            return user_input
        print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Randomly select a choice for the computer."""
    return random.choice(choices)

def determine_winner(user, computer):
    """Determine the winner of a round."""
    if user == computer:
        return 'draw'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return 'user'
    else:
        return 'computer'

def display_scores(scores):
    """Display the current scores."""
    print("\nScores:")
    print(f"User: {scores['user']}")
    print(f"Computer: {scores['computer']}")
    print(f"Draws: {scores['draw']}\n")

def main():
    scores = {'user': 0, 'computer': 0, 'draw': 0}
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            print("Thanks for playing! Final scores:")
            display_scores(scores)
            break

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            print("You win this round!")
            scores['user'] += 1
        elif winner == 'computer':
            print("Computer wins this round!")
            scores['computer'] += 1
        else:
            print("It's a draw!")
            scores['draw'] += 1
        
        display_scores(scores)

# Run the game
if __name__ == "__main__":
    main()
