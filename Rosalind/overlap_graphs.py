import parse_fasta as p


def get_overlap(k, dic):
    '''
    Function that returns a directed graph of nucleotide overlaps
    of size k in the form of an adjacency list

    Arguments
    ---------
    k : int
        The number of nucleotides in the suffix/prefix to consider as
        an overlap
    dic : dictionary
        The dictionary of sequences
        key: string
            the id of the sequence
        value: string
            the sequence

    Returns
    -------
    Adjacency list corresponding to O_k of the form:
    [(id_0, id_2), (id_3, id_4)], where id_n is a string
    '''

    sequences = tuple(dic.values())
    if k > len(sequences[0])/2:
        raise ValueError('k value too big')
    ids = tuple(dic.keys())
    adjacents = []
    # make prefix and suffix tuples
    prefixes, suffixes = \
        (tuple(d) for d in zip(*((seq[0:k], seq[-k::]) for seq in sequences)))

    # find all matches, fill adjacency list
    for i, suf in enumerate(suffixes):
        if suf in prefixes:
            adjacents.extend(
                [(ids[i], ids[j])
                    for j, pre in enumerate(prefixes)
                    if pre == suf and i != j]
                )
    return adjacents


if __name__ == "__main__":
    test = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""
    dic = p.parse_fasta('files/rosalind_grph.txt')
    # dic = p.parse_fasta_string(test)
    for i in get_overlap(3, dic):
        print(i[0] + ' ' + i[1])
