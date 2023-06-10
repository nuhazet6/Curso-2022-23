from __future__ import annotations
import cards
import roles


def get_winner(
    players: list[roles.Player],
    common_cards: list[cards.Card],
    private_cards: list[list[cards.Card]],
) -> tuple[roles.Player | None, cards.Hand]:
    juego = Game(players, common_cards, private_cards)

    return juego.play_round()


class Game:

    def __init__(
        self,
        players: list[roles.Player],
        common_cards: list[cards.Card],
        private_cards: list[list[cards.Card]],
    ):
        self.players = players
        self.common_cards = common_cards
        self.private_cards = private_cards

    def play_round(self):
        for player, private_cards in zip(self.players, self.private_cards):
            player.community_cards = self.common_cards
            player.hole_cards = private_cards
        return self.decide_winner()

    def decide_winner(self) -> tuple[roles.Player | None, cards.Hand]:
        winner = self.players[0]
        is_draw = False
        for player in self.players[1:]:
            if player.best_hand > winner.best_hand:
                is_draw = False
                winner = player
            elif player.best_hand == winner.best_hand:
                is_draw = True
        if is_draw:
            return (None, winner.best_hand)
        return (winner, winner.best_hand)
        # ó return (None, winner.best_hand) if is_draw else (winner,winner.best_hand)
