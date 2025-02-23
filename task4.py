import random

def decide_winner(player_pick, bot_pick):
    if (player_pick == "rock" and bot_pick == "scissors") or \
       (player_pick == "scissors" and bot_pick == "paper") or \
       (player_pick == "paper" and bot_pick == "rock"):
        return "You win!"
    else:
        return "You lose!"

def start_game():
    player_score = 0
    bot_score = 0

    while True:
        print("Welcome to Rock, Paper, Scissors!")
        print("Choose one: rock, paper, or scissors.")

        player_pick = input("Your choice: ").lower()

        if player_pick not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        bot_pick = random.choice(["rock", "paper", "scissors"])
        print(f"Bot chose: {bot_pick}")

        outcome = decide_winner(player_pick, bot_pick)
        print(outcome)

        if outcome == "You win!":
            player_score += 1
        elif outcome == "You lose!":
            bot_score += 1

        print(f"Scores - You: {player_score} | Bot: {bot_score}")

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing!")
            break

start_game()
