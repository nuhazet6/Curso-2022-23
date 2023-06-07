from __future__ import annotations
import helpers

POKER_CARDS={'♣':['🃑','🃒','🃓','🃔','🃕','🃖','🃗','🃘','🃙','🃚','🃛','🃝','🃞'],
'◆':['🃁','🃂','🃃','🃄','🃅','🃆','🃇','🃈','🃉','🃊','🃋','🃍','🃎'],
'❤':['🂱','🂲','🂳','🂴','🂵','🂶','🂷','🂸','🂹','🂺','🂻','🂽','🂾'],
'♠':['🂡','🂢','🂣','🂤','🂥','🂦','🂧','🂨','🂩','🂪','🂫','🂭','🂮']}

class Card:
    SUITS = list(POKER_CARDS.keys())
    CLUBS = SUITS[0]
    DIAMONDS = SUITS[1]
    HEARTS = SUITS[2]
    SPADES = SUITS[3]    
    A_VALUE = 1
    K_VALUE = 13

    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit
    
    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS."""
        return self.value if self.value > Card.A_VALUE else 14

    def __repr__(self):
        """Devuelve el glifo de la carta"""
        return POKER_CARDS[self.suit][self.value - 1]

    def __eq__(self, other: Card | object):
        """Indica si dos cartas son iguales"""
        return self.value == other.value
        
    def __lt__(self, other: Card):
        """Indica si una carta vale menos que otra"""
        return self.cmp_value < other.cmp_value

    def __gt__(self, other: Card):
        """Indica si una carta vale más que otra"""
        return self.cmp_value > other.cmp_value

    def is_ace(self) -> bool:
        """Indica si una carta es un AS"""
        return self.value == Card.A_VALUE

class Deck:
    def __init__(self):
        self.deck = []
        for suit in POKER_CARDS:
            for value in range(len(POKER_CARDS[suit])):
                self.deck.append(Card(value,suit))
        helpers.shuffle(self.deck)

    def __str__(self) -> str:
        return str(self.deck)
    
    def __len__(self):
        return len(self.deck)
    
    def deal_random_card(self,amount:int=1) -> Card:
        rand_index = helpers.randint(0,len(self))
        return self.deck.pop(rand_index)


    def deal_top_cards(self,amount):#¿Hacer cards y devolver una lista?
        return [self.deck.pop(0) for _ in range(amount)]

    def deal_bot_cards(self,amount):
        return [self.deck.pop() for _ in range(amount)]
    
    def shuffle(self):
        helpers.shuffle(self.deck)
    
class Hand:

    def __init__(self,deck):
        HAND_SIZE = 5
        self.cards = deck.deal_top_cards(HAND_SIZE)
        # for _ in range(HAND_SIZE):#Usar con cards y ahorrar el bucle?
        #     self.cards.append(deck.deal_top_card())

    def declare_hand(self,player_cards):
        player_values = [card.cmp_value for card in player_cards]
        higher_player_value = max(player_values)
        HANDS_VALUES = [self.is_royal_stair(player_values,higher_player_value),                
        self.is_straight_flush(player_values,higher_player_value),
        self.is_quads(player_values,higher_player_value)]
        for hand in HANDS_VALUES:
            if hand:
                hand_global_value = len(HANDS_VALUES)-HANDS_VALUES.index(hand)
                hand_value = f'{hand_global_value}.{hand}'
                return float(hand_value)

    def is_royal_stair(self,player_values,higher_player_value):
        return False
    
    def is_straight_flush(self,player_values,higher_player_value):
        return False
    
    def is_quads(self,player_values,higher_player_value):
        card_values = player_values.copy()
        for card in self.cards: #Se puede poner hand_values como property ¿y cachearla?
            card_values.append(card.value)
        for value in card_values:
            if card_values.count(value) == 4 and value in player_values: 
                return f'{value}{higher_player_value:0d}'
        return False
    


dck = Deck()
print(dck, len(dck.deck))
dck.deal_top_cards(52)
print(dck, len(dck.deck))
dck.deck = [Card(5,Card.CLUBS),Card(5,Card.SPADES),Card(5,Card.HEARTS),Card(4,Card.DIAMONDS),Card(6,Card.DIAMONDS)]
hand1 = Hand(dck)
print(hand1.declare_hand([Card(5,Card.DIAMONDS),Card(1,Card.DIAMONDS)]))
