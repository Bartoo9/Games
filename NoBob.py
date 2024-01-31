from NoThanksPlayer import Player 
from NoThanksGame import Card, Deck
from NoThanksState import State
import random

class NoBob(Player):
    def __init__(self):
        Player.__init__(self)
        self.setName("NoBob")
        self.wait_turns = 0

    def take(self, card: Card, state: State):
        collection = [c for c in self.collection]
        c_numbers = [c.number for c in collection]
        coinvalue = 14
        num_players = len(state.players)

        if self.coins <= 0:
            return True
    
        cards_in_deck = 24 - sum(len(player.collection) for player in state.players)
        coins_needed = cards_in_deck / (num_players - 1) * 0.5
        others_coins = sum(player.coins for player in state.players) - self.coins

        if self.coins >= coins_needed + others_coins:
            return False

        
        # Check if the card is in order
        for i in range(len(collection)):
            if card.number == c_numbers[i] + 1:
                if self.wait_turns < 1:
                    self.wait_turns += 1
                    return False
                else:
                    self.wait_turns = 0
                    return True
            
        # Check if we have <= 5 coins, if true, check if the penalty is less than the coin value
        if self.coins <= 5:
            if self.penaltyWhenTake(card) < coinvalue:
                return True
    
        
        # Check if the next player has less than coinvalue/#players coins, if so let him take it
        for player in state.players:
            min_coins = min(player.coins for player in state.players)
            if min_coins <= self.coins * 0.75: 
                if random.random() < 0.5:   
                    return False 
        