from Take5Player import Player
import random
from Take5Game import Row, Card
from Take5State import State, PlayerState
        
class Bob(Player):
    def __init__(self):
        Player.__init__(self)
        self.setName("Bob")
    
    def playCard( self, hand: list[Card], rows: list[Row], state: State ):
        #useful information
        r_targets = [card.goesToRow(rows) for card in hand]
        c_penalties = [card.penalty for card in hand]
        c_numbers = [card.number for card in hand]
        r_lengths = [row.size() for row in rows]

        c_score = [c_penalties[i] + 1/52 * c_numbers[i] + r_lengths[r_targets[i]]
                    for i in range(0,len(hand))]
        return hand[c_score.index(min(c_score))]
    
    def chooseRow( self, rows: list[Row], state: State): 
        r_penalties = [row.penalty() for row in rows]
        r_lengths = [row.size() for row in rows]

        r_score = [r_lengths[i] + r_penalties[i] for i in range(0,4)]
        chooserow = r_score.index(min(r_score))
        return chooserow
    
    


        




         
		