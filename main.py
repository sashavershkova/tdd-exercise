import random

VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    for card in hand: 
        if card not in VALID_CARDS or len(hand) > 5:
            return "Invalid"
        if (card == 'King') or (card == 'Queen') or (card == 'Jack'):
            score += 10
        elif card == 'Ace':
            ace_high = 11
            if score < 21:
                score = ace_high            
        else:
            score += card    
        if score > 21 and 'Ace' in hand:
            score -=10           
    return score