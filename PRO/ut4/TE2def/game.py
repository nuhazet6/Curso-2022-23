from __future__ import annotations
import cards
import roles


def get_winner(
    players: list[roles.Player],
    common_cards: list[cards.Card],
    private_cards: list[list[cards.Card]],
) -> tuple[roles.Player | None, cards.Hand]:
    juego = Game(players)


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

    def play_round(self, show_info: bool = False):  # Meter common_cards
        deck = cards.Deck()
        for player, private_cards in zip(self.players, self.private_cards):
            player.community_cards = self.common_cards
            player.hole_cards = private_cards
        if show_info:
            info = f"Community_cards: "
            for card in self.common_cards:
                info += str(card)
            info += "\n"
            for player in self.players:
                info += f"{str(player)}, {player.best_hand}\n"
            print(info)
        winner_player, winner_hand = self.decide_winner()
        print(f"{winner_player}, {winner_hand}")
        for player in self.players:
            player.return_cards()

    def decide_winner(self) -> tuple[str, cards.Hand]:
        players_hands = ((player.name, player.best_hand) for player in self.players)
        winner_name, winner_hand = next(players_hands)
        is_draw = False
        for player_hand in players_hands:
            hand = player_hand[1]
            if hand > winner_hand:
                is_draw = False
                winner_name, winner_hand = player_hand
            elif hand == winner_hand:
                is_draw = True
        return (
            ("It's a draw", winner_hand)
            if is_draw
            else (f"{winner_name} wins!", winner_hand)
        )
