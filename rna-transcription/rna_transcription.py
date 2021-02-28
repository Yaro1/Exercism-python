dictionary = {"G": "C", "C": "G", "T": "A", "A": "U"}


def to_rna(dna_strand):
    return ''.join([dictionary[i] if i in dictionary else i for i in dna_strand])
