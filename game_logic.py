# game_logic.py
import tkinter as tk
from tkinter import messagebox
import random
from ttkbootstrap import Style

PLAYER_X = "❌"
PLAYER_O = "⭕"

def start_two_player_game():
    start_game(mode="player")

def start_vs_computer_game():
    start_game(mode="computer")

def start_game(mode):
    def on_click(row, col):
        nonlocal current_player, game_over

        if buttons[row][col]["text"] == "" and not game_over:
            buttons[row][col]["text"] = current_player
            board[row][col] = current_player

            if check_winner(current_player):
                messagebox.showinfo("Game Over", f"{current_player} wins!")
                game_over = True
            elif all(all(cell != "" for cell in row) for row in board):
                messagebox.showinfo("Game Over", "It's a draw!")
                game_over = True
            else:
                if mode == "computer" and current_player == PLAYER_X:
                    current_player = PLAYER_O
                    root.after(500, computer_move)
                else:
                    current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

    def computer_move():
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            on_click(row, col)

    def check_winner(player):
        for i in range(3):
            if all(board[i][j] == player for j in range(3)): return True
            if all(board[j][i] == player for j in range(3)): return True
        if all(board[i][i] == player for i in range(3)): return True
        if all(board[i][2 - i] == player for i in range(3)): return True
        return False

    def restart_game():
        nonlocal current_player, game_over, board
        current_player = PLAYER_X
        game_over = False
        board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                buttons[row][col]["text"] = ""

        if mode == "computer" and current_player == PLAYER_O:
            root.after(500, computer_move)

    # Create window
    root = tk.Tk()
    root.title("Tic Tac Toe")

    style = Style(theme='minty')
    frame = tk.Frame(root, bg="white", padx=10, pady=10)
    frame.pack()

    current_player = PLAYER_X
    game_over = False

    board = [["" for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            btn = tk.Button(frame, text="", font=("Arial", 36), width=4, height=2,
                            command=lambda r=row, c=col: on_click(r, c))
            btn.grid(row=row, column=col, padx=5, pady=5)
            buttons[row][col] = btn

    restart_btn = tk.Button(root, text="🔄 Restart Game", font=("Arial", 12), bg="#44c1f0", fg="white", command=restart_game)
    restart_btn.pack(pady=10)

    tk.Label(root, text="© 2025 Rashodha Senevirathne", font=("Arial", 8)).pack(pady=5)

    root.mainloop()
