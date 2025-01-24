import tkinter

# Define player names and colors
PLAYER_1 = 'Player 1'
PLAYER_2 = 'Player 2'
PLAYER_1_SYMBOL = 'X'
PLAYER_2_SYMBOL = 'O'
current_player = PLAYER_1

# Colors
COLOR_BLUE = "#4584b6"
COLOR_YELLOW = "#ffde57"
COLOR_LIGHT_GRAY = "#646464"
COLOR_GRAY = "#343434"

# Initialize game state
turns = 0
game_over = False
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def set_title(row, column):
    global current_player, game_over

    if game_over:
        return

    if board[row][column]["text"] != "":  # Spot already taken
        return

    # Mark the current player's symbol
    if current_player == PLAYER_1:
        board[row][column]["text"] = PLAYER_1_SYMBOL
        current_player_label = PLAYER_2
    else:
        board[row][column]["text"] = PLAYER_2_SYMBOL
        current_player_label = PLAYER_1

    # Update the current player label
    label["text"] = f"{current_player_label}'s turn"
    
    # Switch current player
    current_player = current_player_label

    # Check for a winner
    check_winner()

def check_winner():
    global turns, game_over

    turns += 1

    # Check rows for a winner
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
            declare_winner(board[row][0]["text"])
            highlight_winner([(row, 0), (row, 1), (row, 2)])
            return

    # Check columns for a winner
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                and board[0][column]["text"] != ""):
            declare_winner(board[0][column]["text"])
            highlight_winner([(0, column), (1, column), (2, column)])
            return

    # Check diagonals for a winner
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        declare_winner(board[0][0]["text"])
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        declare_winner(board[0][2]["text"])
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        return

    # Check for a tie
    if turns == 9:
        game_over = True
        label.config(text="It's a tie!", foreground=COLOR_YELLOW)

def declare_winner(symbol):
    global game_over
    winner = PLAYER_1 if symbol == PLAYER_1_SYMBOL else PLAYER_2
    label.config(text=f"{winner} wins!", foreground=COLOR_YELLOW)
    game_over = True

def highlight_winner(positions):
    for row, column in positions:
        board[row][column].config(foreground=COLOR_YELLOW, background=COLOR_LIGHT_GRAY)

def new_game():
    global turns, game_over, current_player

    turns = 0
    game_over = False
    current_player = PLAYER_1

    label.config(text=f"{current_player}'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=COLOR_BLUE, background=COLOR_GRAY)

# Window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=f"{current_player}'s turn", font=("Consolas", 20), background=COLOR_GRAY,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# Setting up the grid buttons for the board
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=COLOR_GRAY, foreground=COLOR_BLUE, width=4, height=1,
                                            command=lambda r=row, c=column: set_title(r, c))
        board[row][column].grid(row=row + 1, column=column)

# Restart button
button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=COLOR_GRAY,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# Center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
