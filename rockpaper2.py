
import random

print("Welcome to a game of Rock, Paper, Scissors")

# User input
rounds = int(input("\nHow many rounds would you like to play: "))

# Initialize variables
moves = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

# Game Loop
for game_round in range(rounds):
    print("\nRound " + str(game_round + 1))
    print("Player: " + str(player_score) + "\tComputer: " + str(computer_score))

    # Computer moves

    c_index = random.randint(0, 2)
    c_choice = moves[c_index]

    # Player move
    player_choice = input("Time to pick........rock, paper, scissors: ").lower().strip()

    #  check for valid moves

    if player_choice in moves:
        print("\tComputer: " + c_choice)
        print("\tPlayer: " + player_choice)

        # Check winner when computer selects rock
        if player_choice == 'rock' and c_choice == 'rock':
            winner = 'tie'
            phrase = 'it is a tie, how boring!'
        elif player_choice == 'paper' and c_choice == 'rock':
            winner = 'player'
            phrase = 'Paper covers rock!'
        elif player_choice == 'scissors' and c_choice == 'rock':
            winner = 'computer'
            phrase = 'Rock smashes scissors!'

    # computer chooses paper
        elif player_choice == 'rock' and c_choice == 'paper':
            winner = 'computer'
            phrase = 'Paper covers rock!'
        elif player_choice == 'paper' and c_choice == 'paper':
            winner = 'tie'
            phrase = 'It is a tie, how boring!'
        elif player_choice == 'scissors' and c_choice == 'paper':
            winner = 'player'
            phrase = 'Scissors cut paper'

    # Computer chooses Scissors
        elif player_choice == 'rock' and c_choice == 'scissors':
            winner = 'player'
            phrase = 'Rock smashes scissors!'
        elif player_choice == 'paper' and c_choice == 'scissors':
            winner = 'computer'
            phrase = 'Scissors cut paper!'
        elif player_choice == 'scissors' and c_choice == 'scissors':
            winner = 'tie'
            phrase = 'It is a tie, how boring'

    # catch other conditions
        else:
            print("Round winner not calculated.")
            winner = 'tie'
            phrase = 'It is a tie, how boring!'

    # Display round result
        print("\t" + phrase)
        if winner == 'player':
            print("\tYou win round " + str(game_round + 1) + ".")
            player_score += 1
        elif winner == 'computer':
            print("\tComputer wins round " +str(game_round + 1) + ".")
            computer_score += 1
        else:
            print("\tThis round is a tie.")

    # Player did not make valid move
    else:
        print("That is not a valid game option!")
        print("Computer gets the point!")
        computer_score += 1

# Print game result
print("\nFinal Game Scores")
print("\tRounds Played: " + str(rounds))
print("\tPlayer Score: " + str(player_score))
print("\tComputer Score: " + str(computer_score))
if player_score > computer_score:
    print("\tWinner:    PLAYER!!!!!")
elif computer_score > player_score:
    print("\tWinner:    Computer.")
else:
    print("\tThe game was a tie.")


