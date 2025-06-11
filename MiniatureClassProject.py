#this is just a miniature class project. 
#this will be a simple tic tac toe game. 

#
import random

from tkinter import Tk, Button, Label, Frame


def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=f"Player {player}'s turn")

            elif check_winner() is True:
                label.config(text=(player + " wins!"))

            elif check_winner() == "Tie":
                label.config(text="It's a Tie!")

        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=f"Player {player}'s turn")

            elif check_winner() is True:
                label.config(text=(player + " wins!"))

            elif check_winner() == "Tie":
                label.config(text="It's a Tie!")
    

def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    # Check columns
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            return True

    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    # Check for tie
    if not empty_spaces():
        return "Tie"

    return False

def empty_spaces():
    return any(buttons[row][col]['text'] == "" for row in range(3) for col in range(3))


def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"Player {player}'s turn")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""

window = Tk()
window.title("Tic Tac Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0], 
          [0,0,0],
          [0,0,0]]
label = Label(text=f"Player {player}'s turn", font=("Arial", 24))
label.pack(side="top")

reset_button = Button(text="Reset", font=('Arial', 24), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('Arial', 24), width=5, height=2,
                                      command=lambda r=row, c=column: next_turn(r, c))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()



