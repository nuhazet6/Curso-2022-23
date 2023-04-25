# ******************
# FIBONACCI ITERABLE
# ******************
class Fibonacci:
    def __init__(self, fibonacci_amount: int):
        self.fibonacci_nums = []
        number1 = 0
        number2 = 1
        for _ in range(fibonacci_amount):
            self.fibonacci_nums.append(number1)
            number1_old = number1
            number1 = number2
            number2 += number1_old
        self.fibonacci_amount = fibonacci_amount
        self.pointer = 0

    def __iter__(self):
        # El iterador es el propio objeto!
        return self

    def __next__(self):
        # Protocolo de iteración
        if self.pointer >= self.fibonacci_amount:
            raise StopIteration
        droid = self.fibonacci_nums[self.pointer]
        self.pointer += 1
        return droid


def run(n: int):
    return list(Fibonacci(n))
