import random

# Initial state of the game board and player settings
board = [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]
currentPlayer = " X "
RunningGame = True

# Function to print the current state of the Tic-Tac-Toe board
def printing(board):
    """
    Prints the current state of the Tic-Tac-Toe board.
    
    Parameters:
    board (list): A list representing the 9 positions of the board.
    
    Returns:
    None
    """
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-------------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-------------")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("-------------")


# Function to get input from Player X and update the board
def user_input(board):
    """
    Takes input from Player X to mark a position on the board.
    
    Parameters:
    board (list): A list representing the 9 positions of the board.
    
    Returns:
    None: Updates the board in place with Player X's move.
    """
    global currentPlayer
    intake = int(input("Player X: Enter a number from 1-9: "))
    if intake >= 1 and intake <= 9 and board[intake - 1] == " - ":
        board[intake - 1] = currentPlayer
    else:
        print("This block is already played or invalid input. Try again.")    
        user_input(board)


# Function to make an automated move for Player O
def automated(board):
    """
    Chooses a random available position on the board for Player O and updates it.
    
    Parameters:
    board (list): A list representing the 9 positions of the board.
    
    Returns:
    None: Updates the board in place with Player O's move.
    """
    global currentPlayer
    while True:
        random_position = random.randint(0, 8)
        if board[random_position] == " - ":
            board[random_position] = currentPlayer
            break


# Function to check if any player has won horizontally
def checkHorizontal(board):
    """
    Checks if any row (horizontal line) has been completed by a player.
    
    Parameters:
    board (list): A list representing the 9 positions of the board.
    
    Returns:
    bool: True if any row has been won by a player, otherwise False.
    """
    global winner
    if board[0] == board[1] == board[2] and board[1] != " - ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != " - ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != " - ":
        winner = board[6]
        return True
    return False


# Function to check if any player has won by columns
def checkRows(board):
    """
    Checks if any column (vertical line) has been completed by a player.
    
    Parameters:
    board (list): A list representing the 9 positions of the board.
    
    Returns:
    bool: True if any column has been won by a player, otherwise False.
    """
    global winner
    if board[0] == board[3] == board[6] and board[3] != " - ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != " - ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5] != " - ":
        winner = board[2]
        return True
    return False


# Function to check if any player has won diagonally
def checkDiagonal(board):
    """
    Checks if any diagonal line has been completed by a player.
    
    Parameters:
    board (list): A list representing the 9 positions of the board.
    
    Returns:
    bool: True if any diagonal has been won by a player, otherwise False.
    """
    global winner
    if board[0] == board[4] == board[8] and board[4] != " - ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != " - ":
        winner = board[2]
        return True
    return False


# Function to check if the game is a tie
def checkTie(board):
    """
    Checks if the board is full and no player has won, indicating a tie.
    
    Parameters:
    board (list): A list representing the 9 positions of the board.
    
    Returns:
    None: If it's a tie, prints a tie message and stops the game.
    """
    global RunningGame
    if " - " not in board:
        printing(board)
        print("It's a tie!")
        RunningGame = False


# Function to switch the current player
def switchPlayer():
    """
    Switches the current player between X and O after each turn.
    
    Parameters:
    None
    
    Returns:
    None: Updates the global currentPlayer variable.
    """
    global currentPlayer
    if currentPlayer == " X ":
        currentPlayer = " O "
    else:
        currentPlayer = " X "


# Function to check if a player has won
def checkWin(board):
    """
    Checks if any player has won by rows, columns, or diagonals.
    
    Parameters:
    board (list): A list representing the 9 positions of the board.
    
    Returns:
    None: If a player wins, prints a winner message and stops the game.
    """
    global RunningGame
    global winner
    if checkDiagonal(board) or checkHorizontal(board) or checkRows(board):
        printing(board)
        print(f"The winner is {winner}!")
        RunningGame = False


# Main function to run the game loop
def main():
    """
    Main game loop that alternates between Player X and Player O moves,
    checks for win or tie conditions, and switches players.
    
    Parameters:
    None
    
    Returns:
    None
    """
    while RunningGame:
        printing(board)
        if currentPlayer == " X ":
            user_input(board)  # Player X's move
        else:
            print("Player O's move (automated):")
            automated(board)  # Player O's move
        
        checkWin(board)  # Check if someone won
        
        if RunningGame:
            checkTie(board)  # Check if it's a tie
            
        if RunningGame:
            switchPlayer()  # Switch players if game is still running


# Entry point to start the game
if __name__ == "__main__":
    main()
