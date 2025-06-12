from tkinter import Tk, Button, Label, Frame
import random

RETRO_BG = "#1e1b3a"          # Deep purple/navy
RETRO_FRAME = "#2b235a"       # Dark indigo
RETRO_BTN = "#00ffd5"         # Neon teal
RETRO_BTN_ALT = "#ff5cc8"     # Hot pink
RETRO_FG = "#00ff90"          # Electric green
RETRO_ACCENT = "#ffe600"      # Neon yellow
FONT_BIG = ("Courier", 28, "bold")
FONT_MED = ("Courier", 18, "bold")

def open_tic_tac_toe():
    menu.destroy()
    tic_tac_toe_game()

def open_connect_four():
    menu.destroy()
    connect_four_game() 

def main_menu():
    global menu
    menu = Tk()
    menu.title("Game Menu")
    menu.configure(bg=RETRO_BG)

    Label(menu, text="Choose a Game", font=FONT_BIG, fg=RETRO_ACCENT, bg=RETRO_BG).pack(pady=20)

    Button(menu, text="Tic Tac Toe", font=FONT_MED, bg=RETRO_BTN, fg="black",
           activebackground=RETRO_BTN_ALT, command=open_tic_tac_toe).pack(pady=10)
    
    Button(menu, text="Connect 4", font=FONT_MED, bg=RETRO_BTN, fg="black",
           activebackground=RETRO_BTN_ALT, command=open_connect_four).pack(pady=10)

    menu.mainloop()

def tic_tac_toe_game():
    def next_turn(row, column):
        nonlocal player
        if buttons[row][column]['text'] == "" and check_winner() is False:
            buttons[row][column]['text'] = player
            result = check_winner()
            if result is False:
                player = players[1] if player == players[0] else players[0]
                label.config(text=f"Player {player}'s turn")
            elif result is True:
                label.config(text=(player + " wins!"))
            elif result == "Tie":
                label.config(text="It's a Tie!")

    def check_winner():
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                return True
        for col in range(3):
            if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
                return True
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            return True
        if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            return True
        if not any(buttons[row][col]['text'] == "" for row in range(3) for col in range(3)):
            return "Tie"
        return False

    def new_game():
        nonlocal player
        player = random.choice(players)
        label.config(text=f"Player {player}'s turn")
        for row in range(3):
            for column in range(3):
                buttons[row][column]['text'] = ""

    def back_to_menu():
        window.destroy()
        main_menu()

    window = Tk()
    window.title("Tic Tac Toe")
    window.configure(bg=RETRO_BG)


    players = ["❌", "⭕"]
    player = random.choice(players)
    buttons = [[0, 0, 0] for _ in range(3)]

    Label(window, text="TIC TAC TOE", font=FONT_BIG, fg=RETRO_ACCENT, bg=RETRO_BG).pack(pady=(15, 5))
    label = Label(window, text=f"Player {player}'s turn", font=FONT_MED, fg=RETRO_FG, bg=RETRO_BG)
    label.pack(pady=(0, 10))

    reset_button = Button(window, text="Reset", font=FONT_MED, bg=RETRO_BTN_ALT, fg="black",
                          activebackground=RETRO_BTN, command=new_game)
    reset_button.pack(pady=(0, 5))

    frame = Frame(window, bg=RETRO_FRAME, bd=5, relief="ridge")
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=FONT_MED, width=5, height=2,
                                          bg=RETRO_BTN, fg="black", activebackground=RETRO_BTN_ALT,
                                          command=lambda r=row, c=column: next_turn(r, c))
            buttons[row][column].grid(row=row, column=column, padx=2, pady=2)

    back_button = Button(window, text="Back to Menu", font=FONT_MED, bg=RETRO_BTN_ALT, fg="black",
                         activebackground=RETRO_BTN, command=back_to_menu)
    back_button.pack(pady=(10, 15))

    window.mainloop()

def connect_four_game():
    # You’ll build this next
    pass


main_menu()
