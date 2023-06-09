from __future__ import annotations
import cards
import game
import roles

player_sample = ("Luis", "Marta", "Juan")

if __name__ == "__main__":
    deck = cards.Deck()
    print(deck)
    common_cards = [deck.deal_top_card() for _ in range(5)]
    private_cards = [[deck.deal_top_card(),
                      deck.deal_top_card()] for player in player_sample]
    players = [roles.Player(name) for name in player_sample]
    table_1 = game.Game(players, common_cards, private_cards)
    winner_player, winner_hand = table_1.play_round(show_info=True)
    print(winner_player, winner_hand)
