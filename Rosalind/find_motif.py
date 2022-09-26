import re


def find_motif(motif, dna):
    """
    Returns list of locations (1-indexed!!!) where the motif was found
    """
    p = re.finditer(f"(?={motif})", dna)
    return [match.start()+1 for match in p]


if __name__ == '__main__':
    f = open('files/rosalind_subs.txt')
    lis = f.read().split('\n')
    print(*find_motif(lis[1], lis[0]))

