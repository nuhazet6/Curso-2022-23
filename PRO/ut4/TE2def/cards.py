from __future__ import annotations
import helpers

SUITS = dict(clubs="♣", diamonds="◆", hearts="❤", spades="♠")

RANKS = 13


class Card:
    def __init__(self, card_repr: str):
        *self.symbol, self.suit = card_repr

    # rank0='2' (lowest), rank12='A' (highest)
    @property
    def rank(self):
        match self.symbol:
            case "J":
                return 9
            case "Q":
                return 10
            case "K":
                return 11
            case "A":
                return 12
            case _:
                return int(self.symbol - 2)

    @property
    def is_ace(self) -> bool:
        return self.rank == 12

    def __str__(self):
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
            for rank in range(RANKS):
                self.cards.append(Card(SUITS[suit], rank))

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

    def __getitem__(self, index: int):
        return self.cards[index]


class Hand:

    RANKINGS = dict(
        royal_flush=9,
        straight_flush=8,
        four_of_a_kind=7,
        full_house=6,
        flush=5,
        straight=4,
        three_of_a_kind=3,
        two_pair=2,
        pair=1,
        high_card=0,
    )

    def __init__(self, *cards: Card):
        self.cards = sorted(cards, reverse=True)
        self._cat = None

    def __str__(self):
        return "".join(str(card) for card in self.cards)

    def __len__(self):
        return len(self.cards)

    @helpers.type_control
    def __gt__(self, other):
        if self.cat == other.ranking:
            for card1, card2 in zip(self.cards, other.cards):
                if card1 == card2:
                    continue
                return card1 > card2
        return self.cat > other.ranking

    @helpers.type_control
    def __eq__(self, other):
        if self.cat == other.ranking:
            for card1, card2 in zip(self.cards, other.cards):
                if card1.rank != card2.rank:
                    break
            else:
                return True
            return False

    def __lt__(self, other):
        return not (self > other)

    def __getitem__(self, index: int):
        return self.cards[index]

    @property
    def cat(self) -> int:
        if self._cat is None:
            is_flush = True
            is_straight = True
            rank_repetitions = []
            repetition_count = 1
            for card1, card2 in zip(self.cards, self.cards[1:]):
                if card1.suit != card2.suit:
                    is_flush = False
                if card1.is_ace:
                    # An ace can make a straight on both ends, rank3='5' and rank11='K'
                    if card2.rank not in (3, 11):
                        is_straight = False
                elif card1.rank != card2.rank + 1:
                    is_straight = False
                if card1.rank == card2.rank:
                    repetition_count += 1
                elif repetition_count > 1:
                    rank_repetitions.append(repetition_count)
                    repetition_count = 1
            if repetition_count > 1:
                rank_repetitions.append(repetition_count)
            # Now a rank is assigned using the information extracted
            if self[0].is_ace and is_flush and is_straight:
                ranking = "royal_flush"
            elif is_flush and is_straight:
                ranking = "straight_flush"
            elif rank_repetitions == [4]:
                ranking = "four_of_a_kind"
            elif rank_repetitions == [3, 2] or rank_repetitions == [2, 3]:
                ranking = "full_house"
            elif is_flush:
                ranking = "flush"
            elif is_straight:
                ranking = "straight"
            elif rank_repetitions == [3]:
                ranking = "three_of_a_kind"
            elif rank_repetitions == [2, 2]:
                ranking = "two_pair"
            elif rank_repetitions == [2]:
                ranking = "pair"
            else:
                ranking = "high_card"
            self._cat = Hand.RANKINGS[ranking]
        return self._cat
