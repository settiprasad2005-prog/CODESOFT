# Rock Paper Scissors Game GUI using Python

import tkinter as tk
import random
from tkinter import messagebox

# Scores
user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

# Game Function
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    # Display choices
    user_choice_label.config(text=f"You Chose: {user_choice}")
    computer_choice_label.config(text=f"Computer Chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie! 🤝"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
        user_score += 1

    else:
        result = "Computer Wins! 🤖"
        computer_score += 1

    # Display result
    result_label.config(text=result)

    # Update score
    score_label.config(
        text=f"Your Score: {user_score}    Computer Score: {computer_score}"
    )

# Reset Game
def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    result_label.config(text="")
    user_choice_label.config(text="")
    computer_choice_label.config(text="")

    score_label.config(text="Your Score: 0    Computer Score: 0")

# Main Window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x450")
root.configure(bg="#f0f0f0")

# Title
title = tk.Label(
    root,
    text="🎮 Rock Paper Scissors",
    font=("Arial", 22, "bold"),
    bg="#f0f0f0",
    fg="#333"
)
title.pack(pady=20)

# Instruction
instruction = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 14),
    bg="#f0f0f0"
)
instruction.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

# Rock Button
rock_btn = tk.Button(
    button_frame,
    text="🪨 Rock",
    width=12,
    font=("Arial", 12, "bold"),
    bg="#ff9999",
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

# Paper Button
paper_btn = tk.Button(
    button_frame,
    text="📄 Paper",
    width=12,
    font=("Arial", 12, "bold"),
    bg="#99ccff",
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

# Scissors Button
scissors_btn = tk.Button(
    button_frame,
    text="✂️ Scissors",
    width=12,
    font=("Arial", 12, "bold"),
    bg="#99ff99",
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=10)

# User Choice Label
user_choice_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="#f0f0f0"
)
user_choice_label.pack(pady=10)

# Computer Choice Label
computer_choice_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="#f0f0f0"
)
computer_choice_label.pack(pady=10)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="purple"
)
result_label.pack(pady=15)

# Score Label
score_label = tk.Label(
    root,
    text="Your Score: 0    Computer Score: 0",
    font=("Arial", 14, "bold"),
    bg="#f0f0f0"
)
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(
    root,
    text="🔄 Play Again",
    font=("Arial", 12, "bold"),
    bg="#ffcc66",
    command=reset_game
)
reset_btn.pack(pady=20)

# Run Application
root.mainloop()