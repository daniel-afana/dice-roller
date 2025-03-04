import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame

class DiceGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Game")
        self.root.geometry("430x400")  # Set the window size

        # Initialize pygame mixer
        pygame.mixer.init()
        self.dice_roll_sound = pygame.mixer.Sound("dice-roll.mp3")

        # Resize dice images to 150x150 pixels
        self.dice_images = [ImageTk.PhotoImage(Image.open(f'dice_png/{i}.png').resize((150, 150))) for i in range(1, 7)]

        self.player_scores = [0, 0]
        self.current_player = 0

        self.dice1_label = tk.Label(root)
        self.dice1_label.grid(row=0, column=0, padx=20, pady=20)

        self.dice2_label = tk.Label(root)
        self.dice2_label.grid(row=0, column=1, padx=20, pady=20)

        self.roll_button = tk.Button(root, text="Roll!", command=self.roll_dice, font=("Helvetica", 20))
        self.roll_button.grid(row=1, column=0, columnspan=2, pady=20)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game, font=("Helvetica", 20))
        self.reset_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.score_label = tk.Label(root, text="Player 1: 0 | Player 2: 0", font=("Helvetica", 20))
        self.score_label.grid(row=3, column=0, columnspan=2, pady=20)

        root.bind('<space>', lambda event: self.roll_dice())

    def roll_dice(self):
        # Play dice roll sound
        self.dice_roll_sound.play()

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        self.dice1_label.config(image=self.dice_images[dice1 - 1])
        self.dice2_label.config(image=self.dice_images[dice2 - 1])

        total = dice1 + dice2
        if dice1 == dice2:
            total *= 2
        self.player_scores[self.current_player] += total

        self.update_score()

        self.current_player = 1 - self.current_player

    def update_score(self):
        self.score_label.config(text=f"Player 1: {self.player_scores[0]} | Player 2: {self.player_scores[1]}")

    def reset_game(self):
        self.player_scores = [0, 0]
        self.current_player = 0
        self.update_score()
        self.dice1_label.config(image='')
        self.dice2_label.config(image='')

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()