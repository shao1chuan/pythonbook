person = ('xiaobai', 18)
print(person[0],person[1])

from collections import namedtuple

Person = namedtuple('Person', 'name age city')        # 类似于定义class
xiaobai = Person(name="xiaobai", age=18, city="paris") # 类似于新建对象
print(xiaobai)


import collections
# 将纸牌定义为具名元组，每个纸牌都有等级和花色
Card = collections.namedtuple('Card', 'rank suit')

class FrenchDeck:
    # 等级2-A
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    # 花色红黑方草
    suits = 'spades diamonds clubs hearts'.split()
    # 构建纸牌
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]


french_deck = FrenchDeck()
print(french_deck.cards[0])
print(french_deck.cards[0].rank)
print(french_deck.cards[0].suit)