import tkinter as tk
from tkinter import messagebox, simpledialog
import random

#Hangamn diplay
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]
#hangman
def hangman_ui():
    
    word = simpledialog.askstring("Word Entry", "Player 1: Enter the word to guess:")
    if word is None:
        messagebox.showinfo("Cancelled", "Word input was cancelled. Exiting Hangman.")
        return  # Exit 
    
    word = word.lower()  #lowercase 
    if not word.isalpha():
        messagebox.showerror("Invalid word", "Please enter a valid word with letters only.")
        return

    hint = simpledialog.askstring("Hint", "Enter a hint (optional):")

    guessed_word = ['_' for _ in word]
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = len(HANGMAN_PICS) - 1

    def make_guess():
        nonlocal wrong_guesses
        guess = letter_input.get().lower()
        letter_input.delete(0, tk.END)

        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single alphabet letter.")
            return

        if guess in guessed_letters:
            messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'.")
            return

        guessed_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            messagebox.showinfo("Correct!", f"'{guess}' is correct!")
        else:
            wrong_guesses += 1
            messagebox.showinfo("Wrong!", f"'{guess}' is not in the word!")

        update_display()

    def update_display():
        word_display.set(' '.join(guessed_word))
        guessed_display.set("Guessed: " + ', '.join(guessed_letters))
        hangman_display.set(HANGMAN_PICS[wrong_guesses])

        if '_' not in guessed_word:
            messagebox.showinfo("Victory!", f"You guessed it! The word was '{word}'.")
            win.destroy()
        elif wrong_guesses >= max_attempts:
            messagebox.showinfo(" Game Over", f"You're hanged! The word was '{word}'.")
            win.destroy()

    win = tk.Toplevel()
    win.title("Hangman Game")

    tk.Label(win, text=" Hangman", font=("Helvetica", 16)).pack(pady=10)

    if hint:
        tk.Label(win, text=f"Hint: {hint}", font=("Helvetica", 12)).pack()

    hangman_display = tk.StringVar()
    hangman_display.set(HANGMAN_PICS[0])
    tk.Label(win, textvariable=hangman_display, font=("Courier", 12), justify="left").pack()

    word_display = tk.StringVar()
    word_display.set(' '.join(guessed_word))
    tk.Label(win, textvariable=word_display, font=("Helvetica", 16)).pack()

    guessed_display = tk.StringVar()
    tk.Label(win, textvariable=guessed_display, font=("Helvetica", 12)).pack()

    letter_input = tk.Entry(win, font=("Helvetica", 14))
    letter_input.pack(pady=5)
    tk.Button(win, text="Guess", command=make_guess).pack(pady=5)
    tk.Button(win, text="Back to Menu", command=win.destroy).pack(pady=10)

    # ROCK, PAPER, SCISSORS
def play_rps_ui():
    player_score = 0
    computer_score = 0

    def play(choice):
        nonlocal player_score, computer_score
        computer = random.choice(['rock', 'paper', 'scissors'])

        if choice == computer:
            result.set(f"🤝 Tie! Both chose {choice}")
        elif (choice == 'rock' and computer == 'scissors') or \
             (choice == 'paper' and computer == 'rock') or \
             (choice == 'scissors' and computer == 'paper'):
            result.set(f"✅ You win! Computer chose {computer}")
            player_score += 1
        else:
            result.set(f"💀 You lose! Computer chose {computer}")
            computer_score += 1

        score_display.set(f"🏆 You: {player_score}   🤖 Computer: {computer_score}")

  
    rps_window = tk.Toplevel()
    rps_window.title("Rock, Paper, Scissors")

    tk.Label(rps_window, text=" Rock, Paper, Scissors", font=("Helvetica", 16)).pack(pady=10)

    btn_frame = tk.Frame(rps_window)
    btn_frame.pack()

    for option in ['rock', 'paper', 'scissors']:
        tk.Button(btn_frame, text=option.capitalize(), width=10, font=("Helvetica", 12),
                  command=lambda opt=option: play(opt)).pack(side="left", padx=10)

    result = tk.StringVar()
    tk.Label(rps_window, textvariable=result, font=("Helvetica", 14)).pack(pady=10)

    score_display = tk.StringVar()
    score_display.set("🏆 You: 0   🤖 Computer: 0")
    tk.Label(rps_window, textvariable=score_display, font=("Helvetica", 12)).pack(pady=5)

    tk.Button(rps_window, text="Back to Menu", command=rps_window.destroy).pack(pady=10)


#ROLL THE DICE 
def roll_dice_ui():
    def roll():
        result = random.randint(1, 6)
        dice_result.config(text=f"You rolled a {result} 🎲")

    dice_window = tk.Toplevel()
    dice_window.title("Roll the Dice")

    tk.Label(dice_window, text="🎲 Roll the Dice", font=("Helvetica", 16)).pack(pady=10)
    tk.Button(dice_window, text="Roll", font=("Helvetica", 14), command=roll).pack(pady=10)
    dice_result = tk.Label(dice_window, text="", font=("Helvetica", 14))
    dice_result.pack(pady=10)
    tk.Button(dice_window, text="Back to Menu", command=dice_window.destroy).pack(pady=5)


# MAIN 
def main_menu_ui():
    root = tk.Tk()
    root.title("Python Game Hub")

    tk.Label(root, text="🎮 Python Game Hub", font=("Helvetica", 20)).pack(pady=20)

    tk.Button(root, text="Hangman", font=("Helvetica", 14), width=25, command=hangman_ui).pack(pady=10)
    tk.Button(root, text="Rock, Paper, Scissors", font=("Helvetica", 14), width=25, command=play_rps_ui).pack(pady=10)
    tk.Button(root, text="Roll the Dice", font=("Helvetica", 14), width=25, command=roll_dice_ui).pack(pady=10)
    tk.Button(root, text="Quit", font=("Helvetica", 14), width=25, command=root.destroy).pack(pady=20)

    root.mainloop()


main_menu_ui()




