class Seq:
    """A sequence"""

    def __init__(self, seq):
        # Property for storing the sequence as a string
        self.strbase = seq

    def __str__(self):
        return self.strbase

    def len(self):
        return len(self.strbase)

    def complement(self):
        # Calculate the complement string from the seq attribute

        # define a dictionay with the complements of the four bases
        base_complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comb = ""  # Create a new empty string
        for i, b in enumerate(self.strbase):
            comb += base_complement[b]
        return Seq(comb)

    def reverse(self):
        return Seq(self.strbase[::-1])

    def count(self, base):
        return self.strbase.count(base)

    def perc(self, base):
        try:
            return round(self.count(base) * 100 / self.len(), 1)
        except ZeroDivisionError:
            return 0
