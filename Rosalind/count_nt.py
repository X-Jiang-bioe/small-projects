from collections import Counter

letters = ['A', 'C', 'G', 'T']


def count_nt(s):
    """
    Returns counts of nt in order: 'A', 'C', 'G', 'T'
    """
    counter = Counter(s)
    counts = [counter[x] for x in letters]
    return(counts)


if __name__ == "__main__":
    f = open('files/rosalind_dna.txt')
    print(*count_nt(f.read()))
