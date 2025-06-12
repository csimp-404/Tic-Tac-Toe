from tkinter import Tk, Button, Label, Frame
import random

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

    Label(menu, text="Choose a Game", font=("Arial", 24)).pack(pady=20)

    Button(menu, text="Tic Tac Toe", font=("Arial", 18), command=open_tic_tac_toe).pack(pady=10)
    Button(menu, text="Connect 4", font=("Arial", 18), command=open_connect_four).pack(pady=10)

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

    players = ["X", "O"]
    player = random.choice(players)
    buttons = [[0, 0, 0] for _ in range(3)]

    label = Label(window, text=f"Player {player}'s turn", font=("Arial", 24))
    label.pack(side="top")

    reset_button = Button(window, text="Reset", font=('Arial', 24), command=new_game)
    reset_button.pack(side="top")

    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=('Arial', 24), width=5, height=2,
                                          command=lambda r=row, c=column: next_turn(r, c))
            buttons[row][column].grid(row=row, column=column)

    back_button = Button(window, text="Back to Menu", font=('Arial, 18'), command=back_to_menu)
    back_button.pack(pady=10)
    
    window.mainloop()

def connect_four_game():
    # You’ll build this next
    pass


main_menu()
