from __future__ import annotations


class IntegerStack:
    def __init__(self, *, max_size: int = 10):
        self.items = []
        self.max_size = max_size

    def push(self, item: int) -> bool:
        """Si la pila está llena retornar False, en otro caso retornar True"""
        if self.is_full():
            return False
        self.items.insert(0, item)
        return True

    def pop(self) -> int:
        """Extraer el elemento que está en el TOP de la pila"""
        return self.items.pop(0)

    def top(self) -> int:
        """Devolver el elemento que está en el TOP de la pila (sin extracción)"""
        return self[0]

    def is_empty(self) -> bool:
        """Indica si la pila está vacía"""
        return len(self) == 0

    def is_full(self) -> bool:
        """Indica si la pila está llena -> max_size"""
        return len(self) >= self.max_size

    def expand(self, factor: int = 2) -> None:
        """Expande el tamaño máximo de la pila en el factor indicado"""
        self.max_size *= factor
        return None

    def dump_to_file(self, path: str) -> None:
        """Vuelca la pila a un fichero. Cada item en una línea"""
        with open(path, "w") as f:
            f.write(str(self))

    @classmethod
    def load_from_file(cls, path: str) -> IntegerStack:
        """Crea una pila desde un fichero. Si la pila se llena al ir añadiendo elementos
        habrá que expandir con los valores por defecto"""
        with open(path, "r") as f:
            new_stack = IntegerStack()
            for item in f:
                if new_stack.is_full():
                    new_stack.expand()
                new_stack.items.insert(len(new_stack), int(item))
            return new_stack

    def __getitem__(self, index: int) -> int:
        """Devuelve el elemento de la pila en el índice indicado"""
        return self.items[index]

    def __setitem__(self, index: int, item: int) -> None:
        """Establece el valor de un elemento de la pila mediante el índice indicado"""
        self.items[index] = item

    def __len__(self):
        """Número de elementos que contiene la pila"""
        return len(self.items)

    def __str__(self):
        """Cada elemento en una línea distinta empezando por el TOP de la pila"""
        return "".join(str(item) + "\n" for item in self.items).strip()

    def __add__(self, other: IntegerStack) -> IntegerStack:
        """La segunda pila va "encima" de la primera"""
        new_size = other.max_size + self.max_size
        new_stack = IntegerStack(max_size=new_size)
        new_stack.items = other.items
        new_stack.items.extend(self.items)
        return new_stack

    def __iter__(self) -> IntegerStackIterator:
        return IntegerStackIterator(self)


class IntegerStackIterator:
    def __init__(self, stack: IntegerStack):
        self.num_items = len(stack)
        self.pointer = 0
        self.items = stack.items

    def __next__(self) -> int:
        if self.pointer >= self.num_items:
            raise StopIteration
        item = self.items[self.pointer]
        self.pointer += 1
        return item
