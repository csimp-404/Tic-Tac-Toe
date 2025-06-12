# app.py

from tkinter import Tk, Button, Label
from style import *
from tic_tac_toe import TicTacToeGame
#from connect_four import ConnectFourGame

class GameApp:
    def __init__(self):
        self.window = None

    def main_menu(self):
        self.window = Tk()
        self.window.title("Game Menu")
        self.window.configure(bg=RETRO_BG)

        Label(self.window, text="Choose a Game", font=FONT_BIG, fg=RETRO_ACCENT, bg=RETRO_BG).pack(pady=20)

        Button(self.window, text="Tic Tac Toe", font=FONT_MED, bg=RETRO_BTN, fg="black",
               activebackground=RETRO_BTN_ALT, command=self.start_tic_tac_toe).pack(pady=10)

        #Button(self.window, text="Connect 4", font=FONT_MED, bg=RETRO_BTN, fg="black",
               #activebackground=RETRO_BTN_ALT, command=self.start_connect_four).pack(pady=10)

        self.window.mainloop()

    def start_tic_tac_toe(self):
        self.window.destroy()
        TicTacToeGame().start(self)

    #def start_connect_four(self):
        #self.window.destroy()
        #ConnectFourGame().start(self)
