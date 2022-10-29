import parse_fasta
import convert_to_RNA
import rna_to_prot
import reverse_compliment
import re

'''
Solution to the Open Reading Frame Problem
'''


def find_starts(rna):
    '''
    finds instances of start codon in rna string
    '''
    return (m.start() for m in re.finditer('(?=AUG)', rna))


def gen_codons(rna, start):
    '''
    creates a generator of codons given an rna string and start position
    '''
    print("working with following sequence:")
    for i in range(start, len(rna), 3):
        print(rna[i:i+3], end=' ')
    print('\n')
    i = 0
    for j in range(start, len(rna), 3):
        yield rna[j:j+3]


def orf(dna):
    '''
    Creates a list of generator objects given a dna string,
    for each reading frame starting at an encountered start codon.

    Each generator returns codons of rna.
    '''
    rdna = reverse_compliment.reverse_compliment(dna)
    rnas = (convert_to_RNA.convert_to_RNA(d) for d in (dna, rdna))
    generators = []
    for rna in rnas:
        for start in find_starts(rna):
            generators.append(gen_codons(rna, start))

    return generators


def get_orf_proteins(dna):
    '''
    Retruns a list of distinct candidate protein strings
    that can be translated from ORFs of dna
    '''
    proteins = set()
    codon_generators = orf(dna)
    for codons in codon_generators:
        print('attempting protein creation')
        prot = rna_to_prot.rna_to_prot(codons)
        if (prot != -1):
            print('protein creation successfull, appending')
            proteins.add(''.join(prot))
        else:
            print('no stop codon identified, moving on')
        print('_______________')

    print(f"ORF analysis complete, {len(proteins)} proteins identified")
    return proteins


if __name__ == '__main__':
    #     test = '''>Rosalind_99
    # AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'''
    # string = tuple(parse_fasta.parse_fasta_string(test).values())[0]
    f = open('files/rosalind_orf.txt')
    string = tuple(parse_fasta.parse_fasta_string(f.read()).values())[0]
    print("\n".join(get_orf_proteins(string)))
