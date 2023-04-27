class DNA:
    VALID_BASES = "ATCG"
    ADENINE = "A"
    THYMINE = "T"
    CYTOSINE = "C"
    GUANINE = "G"

    @property
    def adenines(self):
        return self.sequence.count(DNA.ADENINE)

    @property
    def thymines(self):
        return self.sequence.count(DNA.THYMINE)

    @property
    def cytosines(self):
        return self.sequence.count(DNA.CYTOSINE)

    @property
    def guanines(self):
        return self.sequence.count(DNA.GUANINE)

    def __init__(self, sequence: str):
        self.sequence = sequence.upper()

    def __str__(self) -> str:
        return self.sequence

    def __len__(self):
        return len(self.sequence)

    def __add__(self, other):
        new_sequence = "".join(
            [max(base1, base2) for base1, base2 in zip(self.sequence, other.sequence)]
        )
        remaining_bases = (
            self.sequence[len(other) - len(self) :]
            if len(self) > len(other)
            else (
                other.sequence[len(self) - len(other) :]
                if len(self) < len(other)
                else ""
            )
        )

        return DNA(new_sequence + remaining_bases)

    def __mul__(self, other):
        return DNA(
            "".join(
                [
                    base1
                    for base1, base2 in zip(self.sequence, other.sequence)
                    if base1 == base2
                ]
            )
        )

    def __setitem__(self, index, base):
        result = list(self.sequence)
        result[index] = base if base in DNA.VALID_BASES else "A"
        self.sequence = "".join(result)

    @classmethod
    def build_from_file(cls, path):
        # metodo de clase para construir desde fichero
        with open(path, "r") as f:
            file_text = f.read().strip().replace("\n", "")
        return DNA(file_text)

    def dump_to_file(self, path) -> None:
        # metodo de instancia para volcar la información a un fichero
        with open(path, "w") as f:
            file_text = f.write(self.sequence)

    def stats(self) -> dict:
        all_bases = len(self)
        return dict(
            A=round(self.adenines / all_bases * 100, 3),
            C=round(self.cytosines / all_bases * 100, 3),
            G=round(self.guanines / all_bases * 100, 3),
            T=round(self.thymines / all_bases * 100, 3),
        )

    # Implementar metodo para cambiar la base en x posición


print(DNA.ADENINE)
dna_seq1 = DNA("ATGGT")
print(dna_seq1)
print(dna_seq1.adenines)
print(dna_seq1.cytosines)
print(dna_seq1.guanines)
print(dna_seq1.thymines)
dna_seq2 = DNA("TAAGT")
print(dna_seq1 + dna_seq2)
print(dna_seq1.stats())
print(dna_seq1 * dna_seq2)
dna_seq1[4] = "G"
print(dna_seq1)
dna_seq1[4] = "P"
print(dna_seq1)
