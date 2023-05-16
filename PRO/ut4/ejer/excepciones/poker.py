from __future__ import annotations
import random

def load_card_glyphs(path: str = "cards.dat") -> dict[str, str]:
    """Retorna un diccionario donde las claves serán los palos
    y los valores serán cadenas de texto con los glifos de las
    cartas sin ningún separador"""
    with open(path, "r") as f:
        deck = {}
        for line in f:
            suit, glyphs = line.strip().replace(',','').split(":")
            deck[suit] = glyphs
        return deck


class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOL_VALUE = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13} # list + index?
    A_VALUE = 1
    K_VALUE = 13
    GLYPHS = load_card_glyphs()
    # SYMBOLS_VALUES = dict(zip(SYMBOLS,range(1,len(SYMBOLS)+1)))

    def __init__(self, value: int | str, suit: str):
        """Notas:
        - Si el suit(palo) no es válido hay que elevar una excepción de tipo
        InvalidCardError() con el mensaje: 🃏 Invalid card: {repr(suit)} is not a supported suit
        - Si el value(como entero) no es válido (es menor que 1 o mayor que 13) hay que
        elevar una excepción de tipo InvalidCardError() con el mensaje:
        🃏 Invalid card: {repr(value)} is not a supported value
        - Si el value(como string) no es válido hay que elevar una excepción de tipo
        🃏 Invalid card: {repr(value)} is not a supported symbol

        - self.suit deberá almacenar el palo de la carta '♣◆❤♠'.
        - self.value deberá almacenar el valor de la carta (1-13)"""
        if suit not in Card.get_available_suits():
            raise InvalidCardError(f"{repr(suit)} is not a supported suit")
        if isinstance(value, int):
            if len(Card.SYMBOL_VALUE) < value or value < 1 :
                raise InvalidCardError(f"{repr(value)} is not a supported value")
            self.value = value
        elif isinstance(value,str):
            if value not in Card.SYMBOL_VALUE:
                raise InvalidCardError(f"{repr(value)} is not a supported symbol")
            self.value = Card.SYMBOL_VALUE[value]  
        self.suit = suit
        # self.value = Card.SYMBOLS_VALUES.get(str(value),value)
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self,value):
        self.__value = value
        self.__cmp_value = None
    
    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS."""
        if self.__cmp_value is None:
            self.__cmp_value = self.value if self.value > 1 else 14
        return self.__cmp_value

    def __repr__(self):
        """Devuelve el glifo de la carta"""
        return Card.GLYPHS[self.suit][self.value - 1]

    def __eq__(self, other: Card | object):
        """Indica si dos cartas son iguales"""
        try:
            return self.value == other.value
        except:
            return False
        
    def __lt__(self, other: Card):
        """Indica si una carta vale menos que otra"""
        return self.cmp_value < other.cmp_value

    def __gt__(self, other: Card):
        """Indica si una carta vale más que otra"""
        return self.cmp_value > other.cmp_value

    def __add__(self, other: Card) -> Card:
        """Suma de dos cartas:
        1. El nuevo palo será el de la carta más alta.
        2. El nuevo valor será la suma de los valores de las cartas. Si valor pasa
        de 13 se convertirá en un AS."""
        new_suit = self.suit if self > other else other.suit # o >=
        sum_value = self.cmp_value + other.cmp_value
        new_value = sum_value if sum_value <= 13 else 1
        return Card(new_value, new_suit)

    def is_ace(self) -> bool:
        """Indica si una carta es un AS"""
        return self.value == 1

    @classmethod
    def get_available_suits(cls) -> str:
        """Devuelve todos los palos como una cadena de texto"""
        return cls.CLUBS + cls.DIAMONDS + cls.HEARTS + cls.SPADES

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        """Función generadora que devuelve los glifos de las cartas por su palo"""
        for glyph in cls.GLYPHS[suit]:
            yield glyph


class InvalidCardError(Exception):
    """Clase que representa un error de carta inválida.
    - El mensaje por defecto de esta excepción debe ser: 🃏 Invalid card
    - Si se añaden otros mensajes aparecerán como: 🃏 Invalid card: El mensaje que sea"""
    def __init__(self, message=''):
        self.message = "🃏 Invalid card" 
        if message:
            self.message += f': {message}'
        super().__init__(self.message)

output = load_card_glyphs()
#deck = [i for i in ''.join(output.values())]
suffled_deck = []
for i in ''.join(output.values()):
    index = random.randint(0, len(suffled_deck)) 
    suffled_deck.insert(index,i)
print(suffled_deck)
# print(list(Card.get_cards_by_suit(Card.CLUBS)))
# # card1 = Card(10,Card.CLUBS)
# # print(card1 == 3)