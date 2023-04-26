# ******************
# FIBONACCI ITERABLE
# ******************
class Fibonacci:
    def __init__(self, fibonacci_amount: int):
        self.fibonacci = []
        self.number1 = 0
        self.number2 = 1
        self.num_fibonacci = fibonacci_amount
        self.pointer = 0

    def __iter__(self):
        # El iterador es el propio objeto!
        return self

    def __next__(self):
        # Protocolo de iteración
        if self.pointer >= self.num_fibonacci:
            raise StopIteration
        result = self.number1
        number1_old = self.number1
        self.number1 = self.number2
        self.number2 += number1_old
        self.pointer += 1
        return result


def run(n: int):
    return list(Fibonacci(n))
print(list(Fibonacci(6)))