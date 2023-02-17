import random


def play_game(number_of_candies, player2_type):
    print("Welcome to the Candy Game! There are {} candies on the table.".format(number_of_candies))
    player_turn = random.choice([0, 1])
    print("Player {} will go first.".format(player_turn + 1))

    while number_of_candies > 0:
        if player_turn == 0:
            print("Player 1, it's your turn.")
            candies_taken = int(input("How many candies would you like to take (1-28)? "))
        else:
            if player2_type == "human":
                print("Player 2, it's your turn.")
                candies_taken = int(input("How many candies would you like to take (1-28)? "))
            else:
                print("Player 2 (bot), it's your turn.")
                candies_taken = random.randint(1, 28)
        while candies_taken > 28 or candies_taken < 1:
            candies_taken = int(input("Invalid input. Please enter a number between 1 and 28: "))
        number_of_candies -= candies_taken
        if number_of_candies <= 0:
            print("There are no more candies on the table. Player {} wins!".format(player_turn + 1))
            break
        print("There are now {} candies on the table.".format(number_of_candies))
        player_turn = (player_turn + 1) % 2


play_game(100, "bot")
