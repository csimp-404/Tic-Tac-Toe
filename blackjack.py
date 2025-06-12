# blackjack.py

from tkinter import Tk, Button, Label, Entry, Frame, StringVar
import random
import os
from base_game import BaseGame
from style import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MONEY_FILE = os.path.join(BASE_DIR, "money.txt")

def load_money():
        if os.path.exists(MONEY_FILE):
            with open(MONEY_FILE, "r") as f:
                try:
                    return int(f.read())
                except ValueError:
                    return 500
        return 500
    
def save_money(amount):
    with open(MONEY_FILE,"w") as f:
        f.write(str(amount))


class BlackjackGame(BaseGame):
    
    def __init__(self):
        self.window = None
        self.player_hand = []
        self.dealer_hand = []
        self.money = load_money()
        self.bet = 100

    def start(self, app):
        self.window = Tk()
        self.window.title("Blackjack")
        self.window.configure(bg=RETRO_BG)

        self.status_var = StringVar()
        self.money_var = StringVar()
        self.player_var = StringVar()
        self.dealer_var = StringVar()


        Label(self.window, text="BLACKJACK", font=FONT_BIG, fg=RETRO_ACCENT, bg=RETRO_BG).pack(pady=(10, 5))
        Label(self.window, text="Bet Amount ($):", font=FONT_MED, bg=RETRO_BG, fg=RETRO_FG).pack()

        self.bet_entry = Entry(self.window, font=FONT_MED, justify='center')
        self.bet_entry.insert(0, "100")
        self.bet_entry.pack(pady=5)

        self.money_var.set(f"Money: ${self.money}")
        Label(self.window, textvariable=self.money_var, font=FONT_MED, bg=RETRO_BG, fg=RETRO_ACCENT).pack(pady=(5, 10))

        Button(self.window, text="Deal", font=FONT_MED, bg=RETRO_BTN, fg="black",
               activebackground=RETRO_BTN_ALT, command=self.deal).pack(pady=5)

        self.player_var.set("")
        self.dealer_var.set("")
        Label(self.window, text="Your Hand:", font=FONT_MED, bg=RETRO_BG, fg=RETRO_FG).pack()
        Label(self.window, textvariable=self.player_var, font=FONT_MED, bg=RETRO_BG, fg="white").pack()

        Label(self.window, text="Dealer Hand:", font=FONT_MED, bg=RETRO_BG, fg=RETRO_FG).pack(pady=(10, 0))
        Label(self.window, textvariable=self.dealer_var, font=FONT_MED, bg=RETRO_BG, fg="white").pack()

        Button(self.window, text="Hit", font=FONT_MED, bg=RETRO_BTN, fg="black",
               activebackground=RETRO_BTN_ALT, command=self.hit).pack(pady=(10, 2))
        Button(self.window, text="Stand", font=FONT_MED, bg=RETRO_BTN, fg="black",
               activebackground=RETRO_BTN_ALT, command=self.stand).pack(pady=2)

        Label(self.window, textvariable=self.status_var, font=FONT_MED, bg=RETRO_BG, fg=RETRO_ACCENT).pack(pady=10)

        Button(self.window, text="Back to Menu", font=FONT_MED, bg=RETRO_BTN_ALT, fg="black",
               activebackground=RETRO_BTN, command=lambda: self.back_to_menu(app)).pack(pady=15)

        self.window.mainloop()

    def deal(self):
        try:
            self.bet = int(self.bet_entry.get())
        except ValueError:
            self.status_var.set("Invalid bet amount.")
            return

        if self.bet <= 0 or self.bet > self.money:
            self.status_var.set("Invalid bet size.")
            return

        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card()]
        self.update_display()
        self.status_var.set("Your move: Hit or Stand?")

    def hit(self):
        if not self.player_hand:
            return
        self.player_hand.append(self.draw_card())
        if self.hand_value(self.player_hand) > 21:
            self.end_round("lose")
        else:
            self.update_display()

    def stand(self):
        if not self.player_hand:
            return
        while self.hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.draw_card())

        player_score = self.hand_value(self.player_hand)
        dealer_score = self.hand_value(self.dealer_hand)

        if dealer_score > 21 or player_score > dealer_score:
            self.end_round("win")
        elif player_score == dealer_score:
            self.end_round("draw")
        else:
            self.end_round("lose")

    def draw_card(self):
        return random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

    def hand_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                value += 11
                aces += 1
            else:
                value += int(card)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def update_display(self):
        self.player_var.set(" ".join(self.player_hand) + f"  ({self.hand_value(self.player_hand)})")
        self.dealer_var.set(" ".join(self.dealer_hand) + f"  ({self.hand_value(self.dealer_hand)})")

    def end_round(self, result):
        self.update_display()
        if result == "win":
            self.money += self.bet
            self.status_var.set("You win!")
        elif result == "lose":
            self.money -= self.bet
            self.status_var.set("You lose!")
        else:
            self.status_var.set("Push (draw).")
        self.money_var.set(f"Money: ${self.money}")
        self.player_hand = []
        self.dealer_hand = []
        save_money(self.money)

    def back_to_menu(self, app):
        self.window.destroy()
        app.main_menu()