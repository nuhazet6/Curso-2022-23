from __future__ import annotations
import cards
import roles


class Game:
    def __init__(self, *names: str):
        self.players = [roles.Player(name) for name in names]

    def play_round(self, show_info: bool = False):
        deck = cards.Deck()
        deck.cards = [cards.Card(cards.SUITS['spades'],10),cards.Card(cards.SUITS['clubs'],12),cards.Card(cards.SUITS['clubs'],11),cards.Card(cards.SUITS['clubs'],6)]
        # community_cards = [deck.deal_random_card() for _ in range(5)]
        community_cards = [cards.Card(cards.SUITS['clubs'],10),cards.Card(cards.SUITS['spades'],11),cards.Card(cards.SUITS['hearts'],5),cards.Card(cards.SUITS['hearts'],3),cards.Card(cards.SUITS['diamonds'],2)]
        for player in self.players:
            player.community_cards = community_cards
            player.hole_cards = [deck.deal_top_card() for _ in range(2)]
        if show_info:
            info = f"Community_cards: "
            for card in community_cards:
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