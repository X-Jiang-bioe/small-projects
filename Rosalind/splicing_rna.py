import parse_fasta
import convert_to_RNA
import rna_to_prot
import re

"""
Solution to RNA Splicing problem
Assumes that the first entry of the fasta file is the pre-mRNA
and the subsequent entries are introns
"""


def splice(prem_rna, introns):
    '''
    Splices the pre-mRNA based on given iterable of sequences
    Assumes that the first entry of iterable is the pre-mRNA
    and the subsequent entries are introns
    '''
    # Sort from longest->shortest just in case
    sorted_introns = sorted(introns, key=len, reverse=True)

    # As far as I understand, groups all introns so that
    # there is only one pass of the search
    pattern = re.compile("|".join(sorted_introns))

    mrna = pattern.sub('', prem_rna)
    return mrna


if __name__ == "__main__":
    test = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT"""
    # vals = tuple(parse_fasta.parse_fasta_string(test).values())
    vals = tuple(parse_fasta.parse_fasta('files/rosalind_splc.txt').values())

    t = splice(vals[0], vals[1:])
    rna = convert_to_RNA.convert_to_RNA(t)
    # technically i should have converted to rna first, but honestly the
    # function should work regardless as long as rna is fed with rna introns
    blah = rna_to_prot.rna_to_prot(rna_to_prot.generate_start(rna))

    print(''.join(blah))
