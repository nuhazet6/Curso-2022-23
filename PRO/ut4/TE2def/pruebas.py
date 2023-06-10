from cards import *

dck = Deck()
cards = [dck.deal_top_card() for _ in range(5)]
hand = Hand(*cards)
is_flush = True
is_straight = True
rank_repetitions = []
symbol_repetition = []
cards_symbol = []
repetition_count = 1
for card1, card2 in zip(hand.cards, hand.cards[1:]):
    cards_symbol.append(card1.symbol)
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
cards_symbol.append(card2.symbol)
print(hand, rank_repetitions, cards_symbol)
if len(rank_repetitions) == 1:
    card_index = cards_symbol.index(symbol_repetition[0])
    last_index = card_index + rank_repetitions[0]
    cards = hand.cards[
        card_index:last_index] + hand.cards[:card_index] + hand.cards[
            last_index:]
    hand.cards = cards
    print(hand)
