# main_menu.py
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import game_logic

# Copyright
COPYRIGHT = "© 2025 Rashodha Senevirathne"

def start_game(mode):
    root.destroy()
    if mode == "player":
        game_logic.start_two_player_game()
    else:
        game_logic.start_vs_computer_game()

# GUI Setup
root = tk.Tk()
root.title("Tic Tac Toe - Main Menu")

style = Style(theme='minty')

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

title = ttk.Label(frame, text="🎮 Tic Tac Toe", font=("Helvetica", 24, "bold"))
title.pack(pady=20)

btn_player = ttk.Button(frame, text="Play with Another Player", command=lambda: start_game("player"), width=30)
btn_player.pack(pady=10)

btn_computer = ttk.Button(frame, text="Play with Computer", command=lambda: start_game("computer"), width=30)
btn_computer.pack(pady=10)

footer = ttk.Label(frame, text=COPYRIGHT, font=("Arial", 8))
footer.pack(side="bottom", pady=20)

root.mainloop()
