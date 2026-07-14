import tkinter as tk
from tkinter import messagebox

# ---------------- Window ---------------- #
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("420x500")
root.configure(bg="#2C3E50")
root.resizable(False, False)

# ---------------- Variables ---------------- #
current_player = "X"
board = [""] * 9

winning_combinations = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

# ---------------- Title ---------------- #
title = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 24, "bold"),
    bg="#2C3E50",
    fg="white"
)
title.pack(pady=10)

status = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 16),
    bg="#2C3E50",
    fg="#F1C40F"
)
status.pack()

# ---------------- Game Board ---------------- #
frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=20)

buttons = []


def check_winner():
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != "":
            buttons[a].config(bg="#2ECC71")
            buttons[b].config(bg="#2ECC71")
            buttons[c].config(bg="#2ECC71")
            return True
    return False


def check_draw():
    return "" not in board


def button_click(index):
    global current_player

    if board[index] != "":
        return

    board[index] = current_player

    color = "#3498DB" if current_player == "X" else "#E74C3C"

    buttons[index].config(
        text=current_player,
        fg=color
    )

    if check_winner():
        status.config(text=f"Player {current_player} Wins!")
        messagebox.showinfo("Game Over", f"Player {current_player} Wins!")
        disable_board()
        return

    if check_draw():
        status.config(text="It's a Draw!")
        messagebox.showinfo("Game Over", "It's a Draw!")
        return

    current_player = "O" if current_player == "X" else "X"
    status.config(text=f"Player {current_player}'s Turn")


def disable_board():
    for btn in buttons:
        btn.config(state="disabled")


def new_game():
    global current_player

    current_player = "X"

    for i in range(9):
        board[i] = ""
        buttons[i].config(
            text="",
            bg="white",
            state="normal"
        )

    status.config(text="Player X's Turn")


# Create buttons
for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        width=5,
        height=2,
        font=("Arial", 26, "bold"),
        bg="white",
        relief="ridge",
        command=lambda i=i: button_click(i)
    )

    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# ---------------- New Game Button ---------------- #
new_game_btn = tk.Button(
    root,
    text="New Game",
    font=("Arial", 14, "bold"),
    bg="#27AE60",
    fg="white",
    width=15,
    command=new_game
)

new_game_btn.pack(pady=20)

root.mainloop()