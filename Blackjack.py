import random
import itertools

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


class Game:
    def __init__(self, player: str, player_cash=100, bet=0):
        self.player = player
        self.cash = player_cash
        self.bet = bet

    def placed_bet(self):
        self.player_cash -= self.bet


class Card:
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def __init__(self):

        self.deck = []

    def set_deck(self):
        for suit in self.suits:
            for card in self.cards:
                deck = (suit, card)
                self.deck.append(deck)

    def shuffle(self):
        # found some help making the shuffle feature
        # https://www.programiz.com/python-programming/examples/shuffle-card
        random.shuffle(self.deck)
        print("You've got: ")
        for i in range(2):
            print(self.deck[i][1] , "of", self.deck[i][0])
            Player.hand += self.deck[i][1]
        return Player.hand
            
        # for i in range(2):
        #     draw = (self.deck[i][0], "of", self.deck[i][1])
        #     print(draw)
        #     Dealer.hand.append(self.deck[1][1])

    def hit_me(self, response):
        if Player:
            if response.lower() == "hit":
                random.shuffle(self.deck)
                print("You've got: ")
                for i in range(1):
                    print(self.deck[i][1], "of", self.deck[i][0])
                    Player.hand += self.deck[i][1]
                    return Player.hand
                    
            if Player.hand >= 22:
                print("You've busted")
                Player.hand -= Player.hand
        if Dealer:
            if Dealer.hand >= 17:
                print("Dealer Folds")
                return
            random.shuffle(self.deck)
            print("You've got: ")
            for i in range(1):
                print(self.deck[i][0], "of", self.deck[i][1])
                Dealer.hand += self.deck[i][1]
                return Dealer.hand
            if Dealer.hand >= 22:
                print("Dealer has busted")
                Dealer.hand -= Dealer.hand

    def win_or_lose(self):
        if Dealer.hand > Player.hand:
            return "Dealer's Hand"
        if Dealer.hand > Player.hand:
            print(f"{self.player}'s Hand!")
            pot = Player.bet * 2
            Player.cash += pot
            Player.bet -= Player.bet
            return f"{self.player} You won ${pot} your current cash is ${Player.cash}."


class Player(Card):
    hand = 0

    def __init__(self, player, player_cash=100,):
        super().__init__()
        self.player = player
        self.cash = player_cash

        self.bet = 0

    def placed_bet(self, amount):
        self.bet += amount
        self.cash -= amount

    def player_shuffle(self):
        print("You've got: ")
        for i in range(2):
            self.deck[i][1] , "of", self.deck[i][0]
        return self.hand.append(self.deck[i][1])
    
    def viewhand(self):
        print(self.hand)
        
    def hit_me(self, response):
        if Player:
            if response.lower() == "hit":
                random.shuffle(self.deck)
                print("You've got: ")
                for i in range(1):
                    print(self.deck[i][1], "of", self.deck[i][0])
                    Player.hand += self.deck[i][1]
                    return Player.hand
                    
            if Player.hand >= 22:
                print("You've busted")
                Player.hand -= Player.hand

class Dealer(Card):
    hand = 0

    def __init__(self):
        super().__init__()


def play_blackjack():
    game_deck = Card()
    game_deck.set_deck()
    name = input(
        "Howdy patner! Welcome to The Golden Nugget Cusino! What is your name? ")
    player1 = Player(name)
    while True:
        bet = input(
            f"{player1.player} you currently have much would you like to bet? If you'd like to quit please say quit. ")
        if bet == 'quit':
            break
        else:
            player1.placed_bet(int(bet))
        game_deck.shuffle()
        game_deck.win_or_lose
        ask = input("Would you like to view your hand? ")
        if ask == 'yes':
            player1.viewhand()
        else:
            continue
        game_deck.win_or_lose
        follow_up = input("Would you like to stand or Hit? ")
        if follow_up == "hit":
            player1.hit_me(follow_up)
        else:
            continue
        game_deck.win_or_lose()
        if player1.hand >=22:
            return f"{player1.player} Your hand is {player1.hand}. You lose."
        if Dealer.hand >=22:
            return f"The dealer has busted! you win {player1.player}!"
            


play_blackjack()
