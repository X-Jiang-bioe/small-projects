import re
dic = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }


def rna_to_prot(codons):
    """
    gives list of amino acids of a protein given a codon iterable

    returns -1 if stop codon was not identified or non-iterable is given
    """
    prot = []
    stopped = False
    try:
        for codon in codons:
            try:
                aa = dic[codon]
            # if not a triplet due to reading frame shift
            except KeyError:
                continue
            if aa == "Stop":
                stopped = True
                break
            prot.append(aa)
        if stopped:
            return prot
        else:
            return -1
    # in case of non-iterables i.e. Type error, still return -1
    except TypeError:
        return -1


def generate_start(rna):
    '''
    Generates codons based on the first found start
    regardless of reading frame
    '''
    line = re.search("(AUG).*", rna).group()
    for i in range(0, len(line), 3):
        yield line[i:i+3]


if __name__ == "__main__":
    test = "UCUUACCGGCCACCAUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    f = open('files/rosalind_prot.txt')
    print(''.join(rna_to_prot(generate_start(f.read()))))
