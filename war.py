from random import shuffle


class Card:
    marks=["spades","hearts","diamonds","clubs"]
    values=[None,None,
            "2","3","4","5","6","7","8","9",
            "10","Jack","Queen","King","Ace"]

    def __init__(self,v,m):
        """s and m are Integrate number"""
        self.value=v
        self.mark=m


    def __lt__(self,other):
        if self.value<other.value:
            return True
        if self.value==other.value:
            if self.mark<other.mark:
                return True
            else:
                return False
        return False

    def __gt__(self,other):
        if self.value>other.value:
            return True
        if self.value==other.value:
            if self.mark>other.mark:
                return True
            else:
                return False
        return False


    def __repr__(self):
        v=self.values[self.value]+" of "\
           +self.marks[self.mark]
        return v


class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)


    def rm_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()



class Player:
    def __init__(self,name):
        self.wins=0
        self.card=None
        self.name=name




class Game:
    def __init__(self):
        name1=input("Type your name1:")
        name2=input("Type your name2:")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)


    def wins(self,winner):
        w="{} wins this game."
        w=w.format(winner)
        print(w)

    def draw(self,p1n,p1c,p2n,p2c):
        d="{} draws {} and {} draws {}."
        d=d.format(p1n,p1c,p2n,p2c)
        print(d)



    def play_game(self):
        cards=self.deck.cards
        print("War begin.")
        while len(cards)>=2:
            m="Type q to quit.Type others to play"
            response=input(m)
            if response=="q":
                break
            p1n=self.p1.name
            p2n=self.p2.name
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            self.draw(p1n,p1c,p2n,p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)

        win=self.winner(self.p1,self.p2)
        print("Game end, and {} wins.".format(win))
 

    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return "draw"
    


game=Game()
game.play_game()





    



    
