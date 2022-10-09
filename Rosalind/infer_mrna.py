mil = 1000000
dic = {
    'F': 2, 'L': 6, 'I': 3, 'V': 4, 'M': 1,
    'S': 6, 'P': 4, 'T': 4, 'A': 4, 'Y': 2,
    'H': 2, 'N': 2, 'D': 2, 'Q': 2, 'K': 2,
    'E': 2, 'C': 2, 'R': 6, 'G': 4, 'W': 1,
    'Stop': 3}


def get_possible_num(seq):
    '''
    Returns the total number of different RNA strings
    from which the protein could have been translated,
    modulo 1,000,000
    '''
    i = 1
    for s in seq:
        i *= dic[s]
    return (i * 3) % mil


if __name__ == "__main__":
    f = open('files/rosalind_mrna.txt')
    print(get_possible_num(f.read()))
