import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = Deck.create_deck()  # Use static method to create the deck
        random.shuffle(self.cards)  # Shuffle the deck

    @staticmethod
    def create_deck():
        suits = ["♠", "♥", "♣", "♦"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return [Card(rank, suit) for suit in suits for rank in ranks]

    def show_all(self):
        print(" ".join(str(card) for card in self.cards))

    def draw(self, num_cards):
        if num_cards > len(self.cards):
            raise ValueError("Inte tillräckligt med kort kvar i leken")
        drawn_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return drawn_cards

# Skapa en kortlek
deck = Deck()

print("Alla kort i kortleken:")
deck.show_all()

print("Dra ett kort:")
drawn_card = deck.draw(1)
print(f"Du drog: {drawn_card[0]}")

print("Kvarvarande kort i kortleken:")
deck.show_all()
