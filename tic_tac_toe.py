# tic_tac_toe.py

from tkinter import Tk, Button, Label, Frame
import random
from style import *
from base_game import BaseGame

class TicTacToeGame(BaseGame):
    def __init__(self):
        self.window = None
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.players = ["❌", "⭕"]
        self.player = random.choice(self.players)

    def start(self, app):
        self.window = Tk()
        self.window.title("Tic Tac Toe")
        self.window.configure(bg=RETRO_BG)

        Label(self.window, text="TIC TAC TOE", font=FONT_BIG, fg=RETRO_ACCENT, bg=RETRO_BG).pack(pady=(15, 5))
        self.label = Label(self.window, text=f"Player {self.player}'s turn", font=FONT_MED, fg=RETRO_FG, bg=RETRO_BG)
        self.label.pack(pady=(0, 10))

        Button(self.window, text="Reset", font=FONT_MED, bg=RETRO_BTN_ALT, fg="black",
               activebackground=RETRO_BTN, command=self.new_game).pack(pady=(0, 5))

        frame = Frame(self.window, bg=RETRO_FRAME, bd=5, relief="ridge")
        frame.pack()

        for row in range(3):
            for col in range(3):
                btn = Button(frame, text="", font=FONT_MED, width=5, height=2,
                             bg=RETRO_BTN, fg="black", activebackground=RETRO_BTN_ALT,
                             command=lambda r=row, c=col: self.next_turn(r, c))
                btn.grid(row=row, column=col, padx=2, pady=2)
                self.buttons[row][col] = btn

        Button(self.window, text="Back to Menu", font=FONT_MED, bg=RETRO_BTN_ALT, fg="black",
               activebackground=RETRO_BTN, command=lambda: self.back_to_menu(app)).pack(pady=(10, 15))

        self.window.mainloop()

    def next_turn(self, row, column):
        if self.buttons[row][column]['text'] == "" and not self.check_winner():
            self.buttons[row][column]['text'] = self.player
            result = self.check_winner()
            if not result:
                self.player = self.players[1] if self.player == self.players[0] else self.players[0]
                self.label.config(text=f"Player {self.player}'s turn")
            elif result == "Tie":
                self.label.config(text="It's a Tie!")
            else:
                self.label.config(text=(self.player + " wins!"))

    def check_winner(self):
        b = self.buttons
        for i in range(3):
            if b[i][0]['text'] == b[i][1]['text'] == b[i][2]['text'] != "":
                return True
            if b[0][i]['text'] == b[1][i]['text'] == b[2][i]['text'] != "":
                return True
        if b[0][0]['text'] == b[1][1]['text'] == b[2][2]['text'] != "":
            return True
        if b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text'] != "":
            return True
        if not any(b[r][c]['text'] == "" for r in range(3) for c in range(3)):
            return "Tie"
        return False

    def new_game(self):
        self.player = random.choice(self.players)
        self.label.config(text=f"Player {self.player}'s turn")
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = ""

    def back_to_menu(self, app):
        self.window.destroy()
        app.main_menu()