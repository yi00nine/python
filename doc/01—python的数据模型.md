###### python风格

```python
import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
  
    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
  
    def __getitem__(self,position):
        return self._cards[position]
  


deck = FrenchDeck()

suit_value = dict(spades=3,hearts=2,diamonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)
```

FrenchDeck隐式继承于object类,但功能不是继承来的.通过实现 `__len__` `__getitem__` 两个特殊方法,FrenchDeck就和python自有的序列数据类型一样.特殊方法是被python解释器调用的,你自己不需要去调用他,也就是没有 `my_object.__len__()`这种写法,而应该是用 `len(my_object)`来调用.如果my_object是自定义类的对象,python解释器会去调用由自己实现的 `__len__()`方法,如果是内置的数据类型,python解释器会直接调用PyVarObject里面的ob_size属性

```python
from math import hypot

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'vector(%r.%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(hypot(self.x, self.y))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
```

Vector类的实现模拟了一个数值类型,代码中有六个特殊方法,除了 ` __init__,其他不会在代码的其他地方使用`

- 字符串的表示形式: python有个内置的函数repr(用字符串的形式表现对象),repr就是通过__repr__这个特殊方法来得到对象的字符串表现形式.
- 算术运算符:通过__mul__和__add__实现算数运算符,返回值都是新创建的Vector变量.
- 自定义的bool:为了判定一个值是真还是假,python会调用bool(x),返回True或False.

len()方法为什么不是普通方法而是特殊方法:是为了python自带的数据结构可以更快的运行
