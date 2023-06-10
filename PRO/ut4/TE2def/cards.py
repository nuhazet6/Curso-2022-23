from __future__ import annotations
import helpers

SUITS = dict(clubs="♣", diamonds="◆", hearts="❤", spades="♠")

SYMBOL_VALUE = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


class Card:

    def __init__(self, card_repr: str):
        self.symbol = card_repr[:-1]
        self.suit = card_repr[-1]

    @property
    def rank(self):
        return SYMBOL_VALUE[self.symbol]

    @property
    def is_ace(self) -> bool:
        return self.symbol == 'A'

    def __repr__(self):
        return f"{self.symbol}{self.suit}"

    @helpers.type_control
    def __gt__(self, other):
        return self.rank > other.rank

    @helpers.type_control
    def __eq__(self, other):
        return self.rank == other.rank


class Deck:

    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for symbol in SYMBOL_VALUE:
                self.cards.append(Card(f"{symbol}{SUITS[suit]}"))
        self.shuffle()

    @staticmethod
    def check_empty(method):

        def wrapper(self, *args, **kwargs):
            if len(self) == 0:
                return "Deck is empty"
            else:
                return method(self, *args, **kwargs)

        return wrapper

    @check_empty
    def deal_random_card(self) -> Card:
        return self.cards.pop(helpers.randint(0, len(self) - 1))

    @check_empty
    def deal_top_card(self) -> Card:
        return self.cards.pop(0)

    @check_empty
    def deal_bottom_card(self) -> Card:
        return self.cards.pop()

    @check_empty
    def show_random_card(self) -> Card:
        return self[helpers.randint(0, len(self) - 1)]

    @check_empty
    def show_top_card(self) -> Card:
        return self[0]

    @check_empty
    def show_bottom_card(self) -> Card:
        return self[-1]

    def shuffle(self):
        helpers.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    @check_empty
    def __getitem__(self, index: int):
        return self.cards[index]


class Hand:
    ROYAL_FLUSH = 10
    STRAIGHT_FLUSH = 9
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    def __init__(self, *cards: Card):
        self.cards = sorted(cards, reverse=True)
        self._cat = None
        self._cat_rank = None

    def __repr__(self):
        return "".join(str(card) for card in self.cards)

    def __len__(self):
        return len(self.cards)

    @helpers.type_control
    def __gt__(self, other):
        if self.cat == other.cat:
            for card1, card2 in zip(self.cards, other.cards):
                if card1 == card2:
                    continue
                return card1 > card2
        return self.cat > other.cat

    @helpers.type_control
    def __eq__(self, other):
        if self.cat == other.cat:
            for card1, card2 in zip(self.cards, other.cards):
                if card1.rank != card2.rank:
                    break
            else:
                return True
            return False

    @helpers.type_control
    def __lt__(self, other):
        if self.cat == other.cat:
            for card1, card2 in zip(self.cards, other.cards):
                if card1 == card2:
                    continue
                return card1 < card2
        return self.cat < other.cat

    def __getitem__(self, index: int):
        return self.cards[index]

    def cat_and_rank(self):
        is_flush = True
        is_straight = True
        rank_repetitions = []
        symbol_repetition = []
        repetition_count = 1

        for card1, card2 in zip(self.cards, self.cards[1:]):
            if card1.suit != card2.suit:
                is_flush = False
            if card1.rank != card2.rank + 1:
                is_straight = False
            if card1.rank == card2.rank:
                repetition_count += 1
            elif repetition_count > 1:
                rank_repetitions.append(repetition_count)
                symbol_repetition.append(card1.symbol)
                repetition_count = 1
        if repetition_count > 1:
            rank_repetitions.append(repetition_count)
            symbol_repetition.append(card1.symbol)
        cat_rank = self[0].symbol
        if self[0].is_ace and is_flush and is_straight:
            cat = self.ROYAL_FLUSH
        elif is_flush and is_straight:
            cat = self.STRAIGHT_FLUSH
        elif rank_repetitions == [4]:
            cat = self.FOUR_OF_A_KIND
            cat_rank = symbol_repetition[0]
        elif rank_repetitions == [3, 2]:
            cat = self.FULL_HOUSE
            cat_rank = symbol_repetition[0], symbol_repetition[1]
        elif rank_repetitions == [2, 3]:
            cat = self.FULL_HOUSE
            cat_rank = symbol_repetition[1], symbol_repetition[0]
            self.cards = self.cards[2:] + self.cards[0:2]
        elif is_flush:
            cat = self.FLUSH
        elif is_straight:
            cat = self.STRAIGHT
        elif rank_repetitions == [3]:
            cat = self.THREE_OF_A_KIND
            cat_rank = symbol_repetition[0]
        elif rank_repetitions == [2, 2]:
            cat = self.TWO_PAIR
            cat_rank = symbol_repetition[0], symbol_repetition[1]
            if self[0].symbol != symbol_repetition[0]:
                self.cards = self.cards[1:] + [self.cards[0]]
            elif self[2].symbol != symbol_repetition[1]:
                self.cards = self.cards[0:2] + self.cards[3:] + [self.cards[2]]
        elif rank_repetitions == [2]:
            cat = self.ONE_PAIR
            cat_rank = symbol_repetition[0]
        else:
            cat = self.HIGH_CARD
        if len(rank_repetitions) == 1:
            #Bloque para ordenar la mano en caso de pareja, trío o póquer
            card_index = [card.symbol
                          for card in self.cards].index(symbol_repetition[0])
            last_index = card_index + rank_repetitions[0]
            cards = self.cards[
                card_index:last_index] + self.cards[:card_index] + self.cards[
                    last_index:]
            self.cards = cards
        return cat, cat_rank

    @property
    def cat(self) -> int:
        if self._cat is None:
            self._cat, self._cat_rank = self.cat_and_rank()
        return self._cat

    @property
    def cat_rank(self) -> int:
        if self._cat_rank is None:
            self._cat, self._cat_rank = self.cat_and_rank()
        return self._cat_rank
