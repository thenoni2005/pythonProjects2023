from cards import *
from player_file import *
from commonGameFunctions import *

class JackBlackDeck(BaseDeck):

    def __init__(self):
        super(JackBlackDeck, self).__init__()
        self.populate()
        self.shuffle()


    def populate(self):
        for suit in JackBlackCard.SUITS:
            for rank in JackBlackCard.RANKS:
                card = JackBlackCard(rank, suit)
                self.cards.append(card)

class JackBlackCard(BaseCard):
    ACEVALUE = 1

    @property
    def value(self):
        if self.isFaceUp:
            val = JackBlackCard.RANKS.index(self.rank)+1
            if val > 10:
                val = 10
        else:
            val = None

            return val

class JackBlackHand(BaseHand):

    @property
    def total(self):

        for card in self.cards:
            if not card.value:

                return None

        # add up cards values treat each ace as one
        t = 0
        for card in self.cards:
            t += card.value


        haveAce = False
        for card in self.cards:
            if card.value == JackBlackCard.ACEVALUE:
                haveAce = True
        if haveAce and t <= 11:
            t += 10

        return t

    def __str__(self):
        ret = BaseHand.__str__(self)
        ret += str(self.name)+"\n"
        ret += str(self.total)+"\n"

        return ret

    def isBusted(self):
        return self.total>=21

    def flipHand(self):
        for card in self.cards:
            card.isFaceup = True

class JackBlackPlayer(JackBlackHand):
    def isHitting(self):
        response = ask_yes_no("\n" + self.name + ", do you want a hit (Y/N): ")
        return response == "y"
    def lose(self):
        print(self.name, "loses.")
    def win(self):
        print(self.name, "wins.")
    def push(self):
        print(self.name, "pushes.")
    def bust(self):
        print(self.name, "busts.")
        self.lose()


class JackBlackDealer(JackBlackHand):
    def isHitting(self):
        soft = True
        for card in self.cards:
            if card .value >= 10:
                soft = False
            if self.total < 17 or (self.total == 17 and soft):
                return True
            else:
                return False

    def bust(self):
        print(self.name, "busts.")

    def flipFirstCard(self):
        firstCard = self.cards[0]
        firstCard.flip()

class JackBlackGames(object):


    def __init__(self,playerNames):
        self.dealer = JackBlackDealer("Dealer  'his name is hector'")
        self.deck = JackBlackDeck()
        self.players = []

        for name in playerNames:
            self.players.append(JackBlackPlayer(name))

    @property
    def stillPlaying(self):
        sp = []
        for player in self.players:
            if not player.isBusted():
                sp.append(player)
        return sp

    def additional_cards(self,player):
        while not player.isBusted() and player.ishitting():
            self.deck.deal([player])
            player.flipHand()
            print(player)
            if player.isBusted():
                player.bust()

    def play(self):
        self.deck.deal(self.players+[self.dealer],perHand=2)
        self.dealer.flipFirstCard()

        for hand in self.players:
            hand.flipHand()

        for player in self.players:
            print(player)

        print(self.dealer)

        for player in self.players:
            print(player)
            self.additional_cards(player)

        self.dealer.flipHand()
        print(self.dealer)
        if self.stillPlaying:

            self.additional_cards(self.dealer)

        if self.dealer.isBusted():
            for player in self.stillPlaying:
                player.win()

        else:
            for player in self.stillPlaying:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                else:
                    player.push()

        for player in self.players:
            player.clearHand()
        self.dealer.clearHand()

