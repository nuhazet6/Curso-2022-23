class DNA:
    ADENINE = "A"
    THYMINE = "T"
    CYTOSINE = "C"
    GUANINE = "G"

    def __init__(self, dna_sequence: str):
        self.dna_sequence = dna_sequence.upper()

    def __str__(self) -> str:
        return self.dna_sequence

    @property
    def count_adenine(self):
        return self.dna_sequence.count(DNA.ADENINE)

    @property
    def count_thymine(self):
        return self.dna_sequence.count(DNA.THYMINE)

    @property
    def count_cytosine(self):
        return self.dna_sequence.count(DNA.CYTOSINE)

    @property
    def count_guanine(self):
        return self.dna_sequence.count(DNA.GUANINE)

    def __add__(self):

dna_seq1 = DNA("AAAGTCTTGAC")
print(dna_seq1)
print(dna_seq1.count_adenine)
print(dna_seq1.count_cytosine)
print(dna_seq1.count_guanine)
print(dna_seq1.count_thymine)
dna_seq2 = DNA("GAAGTCTTGAT")

