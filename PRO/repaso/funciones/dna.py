from __future__ import annotations


class DNA:
    ADENINE = 'A'
    CYTOSINE = 'C'
    GUANINE = 'G'
    THYMINE = 'T'
    VALID_BASES = [ADENINE, CYTOSINE, GUANINE, THYMINE]
    def __init__(self, sequence: str):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    @property
    def adenines(self):
        return self.sequence.count(DNA.ADENINE)

    @property
    def cytosines(self):
        return self.sequence.count(DNA.CYTOSINE)

    @property
    def guanines(self):
        return self.sequence.count(DNA.GUANINE)

    @property
    def thymines(self):
        return self.sequence.count(DNA.THYMINE)

    def __add__(self, other: DNA)-> DNA:
        remain_bases_amount = abs(len(self) - len(other))
        filler = 'A'*remain_bases_amount
        new_sequence = ''
        for base1,base2 in zip(self.sequence+filler,other.sequence+filler):
            new_sequence += base1 if base1 > base2 else base2
        return DNA(new_sequence)

    def __len__(self) -> int:
        return len(self.sequence)

    def stats(self) -> dict[str, float]:
        stat_adenine = self.adenines / len(self) * 100
        stat_cytosine = self.cytosines / len(self) * 100
        stat_guanine = self.guanines / len(self) * 100
        stat_thymines = self.thymines / len(self) * 100
        return {DNA.ADENINE:stat_adenine,DNA.CYTOSINE:stat_cytosine,DNA.GUANINE:stat_guanine,DNA.THYMINE:stat_thymines}

    def __mul__(self, other):
        new_sequence = ''
        for base1,base2 in zip(self.sequence,other.sequence):
            if base1 == base2:
                new_sequence += base1
        return DNA(new_sequence)
        

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        with open(path,'r') as f:
            return DNA(f.read().strip().replace('\n',''))

    def dump_to_file(self, path: str) -> None:
        with open(path,'w') as f:
            f.write(self.sequence)

    def __getitem__(self, index: int) -> str:
        return self.sequence[index]

    def __setitem__(self, index: int, base: str) -> None:
        if not (-len(self) <= index < len(self)):
            raise IndexError('index out of range')
        if base not in DNA.VALID_BASES:
            base = DNA.ADENINE
        self.sequence = self.sequence[:index] + base + self.sequence[index + 1 :]

dna1 = DNA('CGTCAAACTGCA')
dna1[-len(dna1)] = 'A'
print(dna1)