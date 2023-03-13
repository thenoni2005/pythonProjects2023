
class BaseCard():
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣","♠","♥","♦"]

    def __init__(self,rank,suit):
        """Constructor; this is called to build an object from this class"""

        self.isFaceUp = False
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Return a string representation of an object"""
        ret = ""
        if self.isFaceUp:
            ret = str.format("""
            -----------------
            | {0:2}{1}          |
            |               |
            |               |
            |               |            
            |          {1}{0:2} |            
            -----------------
            """, self.rank, self.suit)
        else:
            ret = """
            -----------------
            |***************|
            |***************|
            |***************|
            |***************|
            |***************|                      
            -----------------
                            """
        return ret


    def flip(self):
        """Toggles the isFaceUp bool value to true or false"""
        self.isFaceUp = not self.isFaceUp

    @property
    def value(self):
        if self.isFaceUp:
            return BaseCard.RANKS.index(self.rank)+1
        else:
            return 0


if __name__ == "__main__":
    print("this is not a program try importing and using the classes")
    input("\n\nPress the enter key to exit")



