import cards
class Dealer:
    def __init__(self,deck,players:list):
        self.players = players
        self.deck = deck
    def deal_player_cards(self):
        for player in self.players:
            player.cards.extend(self.deck.deal_top_card(2))#Hacer con cards y ahorrar 

class Player:
    def __init__(self,name,community_cards):
        self.cards = []
        self.community_cards = community_cards
        self.name = name
