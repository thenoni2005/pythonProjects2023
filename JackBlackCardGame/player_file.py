from cards import *
import random

class BaseHand():

    def __init__(self, name):
        self.cards = []
        self.name = name

    def addCard(self,card):
        self.cards.append(card)

    def giveCard(self,card,otherHand):
        self.cards.remove(card)
        otherHand.addCard(card)

    def flipAllCards(self):
        for card in self.cards:
            card.flip()

    def clearHand(self):
        self.cards = []

    def __str__(self):
        ret=""
        if self.cards:
            for card in self.cards:
                ret+=str(card)
        else:
            ret = "<EMPTY>"

        return ret

class BaseDeck(BaseHand):
    def __init__(self):
        self.cards = []

    def populate(self):
        for suit in BaseCard.SUITS:
            for rank in BaseCard.RANKS:
                card = BaseCard(rank, suit)
                self.cards.append(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, handsList, perHand = 1):
        cardsNeeded = len(handsList)*perHand
        if(self.amount >= cardsNeeded):
            for rounds in range(perHand):
                for hand in handsList:
                    topCard = self.cards[0]
                    self.giveCard(topCard,hand)
        else:
            for hand in handsList:
                hand.clearHand()
            self.clearHand()
            self.populate()
            self.shuffle()
            self.deal(handsList, perHand)

    @property
    def amount(self):
        return len(self.cards)




if __name__ == "__main__":
    print("this is not a program try importing and using the classes")
    input("\n\nPress the enter key to exit")