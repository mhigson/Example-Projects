# Player 1 = X
# Player 2 = O
# User input = "row,column"
# Use .split() to transcribe user input, using the "," as the separator.

saved_game = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
player_1_wins = 0
player_2_wins = 0


def check_winner(game):
    for x in range(0, 3):
        row = set([game[x][0], game[x][1], game[x][2]])
        if len(row) == 1 and game[x][0] != 0:
            return game[x][0]
    for x in range(0, 3):
        column = set([game[0][x], game[1][x], game[2][x]])
        if len(column) == 1 and game[0] != 0:
            return game[0][x]
    diag_1 = set([game[0][2], game[1][1], game[2][0]])
    diag_2 = set([game[0][0], game[1][1], game[2][2]])
    if len(diag_1) == 1 or len(diag_2) == 1 and game[1][1] != 0:
        return game[1][1]
    return 0


def user_moves(game):
    global saved_game
    global ticker
    global player_1_wins
    global player_2_wins
    ticker = 1
    while ticker < 9 and check_winner(game) == 0:
        if (ticker % 2) == 1:
            player_1 = input("PLAYER 1 - Enter 'row,column': ").split(",")
            player_1_row = int(player_1[0]) - 1
            player_1_col = int(player_1[1]) - 1
            if game[player_1_row][player_1_col] == 0:
                ticker += 1
                game[player_1_row][player_1_col] = "X "
                print("-" * 13)
                print(str(game[0]).replace("[", "| ").replace("]", "|").replace("'", "").replace(",", "|").replace("0", "  "))
                print("-" * 13)
                print(str(game[1]).replace("[", "| ").replace("]", "|").replace("'", "").replace(",", "|").replace("0", "  "))
                print("-" * 13)
                print(str(game[2]).replace("[", "| ").replace("]", "|").replace("'", "").replace(",", "|").replace("0", "  "))
                print("-" * 13)
            else:
                print("Error: Please choose a blank space.")
        elif (ticker % 2) == 0:
            player_2 = input("PLAYER 2 - Enter 'row,column': ").split(",")
            player_2_row = int(player_2[0]) - 1
            player_2_col = int(player_2[1]) - 1
            if game[player_2_row][player_2_col] == 0:
                ticker += 1
                game[player_2_row][player_2_col] = "O "
                print("-" * 13)
                print(str(game[0]).replace("[", "| ").replace("]", "|").replace("'", "").replace(",", "|").replace("0", "  "))
                print("-" * 13)
                print(str(game[1]).replace("[", "| ").replace("]", "|").replace("'", "").replace(",", "|").replace("0", "  "))
                print("-" * 13)
                print(str(game[2]).replace("[", "| ").replace("]", "|").replace("'", "").replace(",", "|").replace("0", "  "))
                print("-" * 13)
            else:
                print("Error: Please choose a blank space.")
    else:
        if check_winner(saved_game) == "X ":
            print("\n" + "--- Player 1 wins!" + "\n")
            player_1_wins += 1
        elif check_winner(saved_game) == "O ":
            print("--- Player 2 wins!" + "\n")
            player_2_wins += 1
        else:
            print("\n" + "--- Draw " + ("-" * 9) + ("-" * (len(str(player_1_wins)))))
        print("--- Player 1: " + str(player_1_wins) + " ---")
        print("--- Player 2: " + str(player_2_wins) + " ---" + "\n")
        user_input = input("Enter '1' for a rematch or '2' to end the program: ")
        if user_input == str(1):
            print("\n" * 15)
            saved_game = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]
            ticker = 1
            user_moves(saved_game)
        elif user_input == str(2):
            print(end="")


user_moves(saved_game)
