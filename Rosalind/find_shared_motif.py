import parse_fasta

"""
Solution for Finding a Shared Motif problem
this approach is pretty fast, but slightly hard to comprehend
"""


def frame_generator(seq, size):
    """
    Makes a generator of substrings iterating through sequence
    with frame size of size
    """
    for frame in range(len(seq)+1-size):
        yield seq[frame: frame+size], frame


def present_all(sub, sequences):
    # returns True if substring is in all sequences

    return all(map(lambda sequence: sub in sequence, sequences))


def find_motif(sequences):
    # use the shortest sequence as a basis for the search
    base = sorted(sequences, key=len, reverse=False)[0]
    current = base[0]
    current_pos = 0
    for size in range(1, len(base)+1, 1):
        # check if smaller substring size search found nothing
        if len(current)+1 < size:
            return current
        # check if simply extending substring suffix does the trick
        elif present_all(base[current_pos: current_pos+size], sequences):
            current = base[current_pos: current_pos+size]
            continue
        # if above fails, start full search
        else:
            for sub, pos in frame_generator(base, size):
                if len(sub) < size:
                    break
                if present_all(sub, sequences):
                    current = sub
                    current_pos = pos
                    break
    return current


if __name__ == '__main__':
    test = '''>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA'''
    # vals = tuple(parse_fasta.parse_fasta_string(test).values())
    vals = tuple(
        parse_fasta.parse_fasta("files/rosalind_lcsm (1).txt").values())
    print(find_motif(vals))
