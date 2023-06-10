from __future__ import annotations
import cards
import game
import roles

player_sample = ("Luis", "Marta", "Juan")

if __name__ == "__main__":
    deck = cards.Deck()
    common_cards = [deck.deal_top_card() for _ in range(5)]
    private_cards = [[deck.deal_top_card(),
                      deck.deal_top_card()] for _ in player_sample]
    players = [roles.Player(player_name) for player_name in player_sample]
    winner_player, winner_hand = game.get_winner(players, common_cards,
                                                 private_cards)
    print(private_cards)
    print(common_cards)
    print(winner_player, winner_hand)
