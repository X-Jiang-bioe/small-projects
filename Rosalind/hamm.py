def hamm(dna1, dna2):
    """
    returns the Hamming distance given 2 DNA strands
    """
    lis = list(map(issame, dna1, dna2))
    return sum(lis)


def issame(s1, s2):
    if s1 == s2:
        return 0
    else:
        return 1


if __name__ == "__main__":
    f = open('files/rosalind_hamm.txt')
    lis = f.read().split('\n')
    print(hamm(lis[0], lis[1]))
