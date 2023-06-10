from __future__ import annotations
import cards
import helpers


class Player:

    def __init__(self, name: str):
        self.name = name
        self.hole_cards = []
        self.community_cards = []
        self._best_hand = None

    def return_cards(self):
        self.hole_cards = []
        self.community_cards = []

    @property
    def best_hand(self) -> cards.Hand:
        if self._best_hand is None:
            card_combinations = helpers.combinations(
                (*self.hole_cards, *self.community_cards), n=5)
            best_hand = cards.Hand(*next(card_combinations))
            for card_combination in card_combinations:
                hand = cards.Hand(*card_combination)
                if hand > best_hand:
                    best_hand = hand
            self._best_hand = best_hand
        return self._best_hand

    def __str__(self):
        hole_cards = ""
        for card in self.hole_cards:
            hole_cards += str(card)
        return f"{self.name}, {hole_cards}"
