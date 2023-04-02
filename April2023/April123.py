# Texas Hold'em is a Poker variant in which each player is given two "hole cards". Players then proceed to make a series of bets while five "community cards" are dealt. If there are more than one player remaining when the betting stops, a showdown takes place in which players reveal their cards. Each player makes the best poker hand possible using five of the seven available cards (community cards + the player's hole cards).

# Possible hands are, in descending order of value:

# Straight-flush (five consecutive ranks of the same suit). Higher rank is better.
# Four-of-a-kind (four cards with the same rank). Tiebreaker is first the rank, then the rank of the remaining card.
# Full house (three cards with the same rank, two with another). Tiebreaker is first the rank of the three cards, then rank of the pair.
# Flush (five cards of the same suit). Higher ranks are better, compared from high to low rank.
# Straight (five consecutive ranks). Higher rank is better.
# Three-of-a-kind (three cards of the same rank). Tiebreaker is first the rank of the three cards, then the highest other rank, then the second highest other rank.
# Two pair (two cards of the same rank, two cards of another rank). Tiebreaker is first the rank of the high pair, then the rank of the low pair and then the rank of the remaining card.
# Pair (two cards of the same rank). Tiebreaker is first the rank of the two cards, then the three other ranks.
# Nothing. Tiebreaker is the rank of the cards from high to low.
# Given hole cards and community cards, complete the function hand to return the type of hand (as written above, you can ignore case) and a list of ranks in decreasing order of significance, to use for comparison against other hands of the same type, of the best possible hand.

# hand(["A♠", "A♦"], ["J♣", "5♥", "10♥", "2♥", "3♦"])
# # ...should return ("pair", ranks: ["A", "J", "10", "5"]})
# hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"])
# # ...should return ("flush", ["Q", "J", "10", "5", "3"])

def hand(hole_cards, community_cards):
    # Create a list of all seven cards
    all_cards = hole_cards + community_cards

    # Create a dictionary to count the number of cards of each rank
    rank_counts = {}
    for card in all_cards:
        rank = card[0]
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1

    # Check for a straight or a straight flush
    ranks = "AKQJT98765432A"
    straight_indices = [(ranks.index(r) + 1) % len(ranks) for r in rank_counts.keys()]
    straight_indices.sort()
    straight_possible = False
    for i in range(len(straight_indices) - 4):
        if straight_indices[i:i+5] == list(range(straight_indices[i], straight_indices[i]+5)):
            straight_possible = True
            break
    flush_possible = any([sum([card[-1] == suit for card in all_cards]) >= 5 for suit in "♠♥♦♣"])
    if straight_possible and flush_possible:
        # Straight-flush
        straight_flush_rank = ranks[straight_indices[i]+4]
        return ("straight-flush", [straight_flush_rank])

    # Check for four-of-a-kind
    four_of_a_kind_rank = None
    remaining_rank = None
    for rank, count in rank_counts.items():
        if count == 4:
            four_of_a_kind_rank = rank
        elif count == 1:
            remaining_rank = rank
    if four_of_a_kind_rank is not None:
        return ("four-of-a-kind", [four_of_a_kind_rank, remaining_rank])

    # Check for full house
    three_of_a_kind_rank = None
    pair_rank = None
    for rank, count in rank_counts.items():
        if count == 3:
            three_of_a_kind_rank = rank
        elif count == 2:
            pair_rank = rank
    if three_of_a_kind_rank is not None and pair_rank is not None:
        return ("full house", [three_of_a_kind_rank, pair_rank])

    # Check for flush
    flush_cards = []
    for suit in "♠♥♦♣":
        suit_cards = [card for card in all_cards if card[-1] == suit]
        if len(suit_cards) >= 5:
            suit_cards.sort(key=lambda c: ranks.index(c[0]), reverse=True)
            flush_cards = suit_cards[:5]
            break
    if flush_cards:
        return ("flush", [card[0] for card in flush_cards])

    # Check for straight
    if straight_possible:
        straight_rank = ranks[straight_indices[i]+4]
        return ("straight", [straight_rank])

    # Check for three-of-a-kind
    three_of_a_kind_rank = None
    remaining_ranks = []
    for rank, count in rank_counts.items():
        if count == 3:
            three_of_a_kind_rank = rank
        elif count == 1:
            remaining_ranks.append(rank)
    if three_of_a_kind_rank is not None:
        remaining_ranks.sort(key=lambda r: ranks.index(r), reverse=True)
        return ("three-of-a-kind", [three_of_a_kind_rank] + remaining_ranks[:2])

    # Check for two pair
    pair_ranks = []
    remaining_rank = None
    for rank
