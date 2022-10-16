import re
import parse_fasta as parse
import requests


def find_motif(motif, sequence):
    """
    Solution for finding motif in DNA

    Returns list of locations (1-indexed!!!) where the motif was found
    """
    p = re.finditer(f"(?={motif})", sequence)
    return (match.start()+1 for match in p)


def find_nglycosylation(ids):
    '''
    Solution for Finding Protein Motif problem

    Finds N-Glycosilatiion motifs' locations (1-indexed)
    within a protein string given the uniprot IDs of said proteins.

    Retruns
    -------
    generator object with each element of the form:
    ('id', (motif_loc1, motif_loc2,...))
    '''
    link_l = "https://rest.uniprot.org/uniprotkb/"
    link_r = ".fasta"

    motif_reg = "[N][^P][S,T][^P]"
    idtrim_reg = ".*?(?=(_))"
    # id_reg = "\\|(.*?)\\|"
    fas = ""
    with requests.Session() as s:
        for id in ids:
            match = re.search(idtrim_reg, id)
            # If id has extraneous modifiers (XXXX_modifier_modiefier2)
            if match:
                # strip modifiers
                id = match[0]
            # put protein seq. in list
            r = s.get(link_l + id + link_r)
            fas += r.text

    # process whole thing in a batch
    strings = tuple(parse.parse_fasta_string(fas).values())

    locs = \
        ((id, tuple(find_motif(motif_reg, s))) for id, s in zip(ids, strings))

    return locs


if __name__ == '__main__':
    # commented out the 'finding motif in DNA' problem stuff
    # f = open('files/rosalind_subs.txt')
    # lis = f.read().split('\n')
    # print(*find_motif(lis[1], lis[0]))

    # 'finding protein motif' problem below
    test = """A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST"""
    # lis = test.split("\n")
    f = open('files/rosalind_mprt.txt')
    lis = f.read().split('\n')

    for pair in find_nglycosylation(lis):
        if len(pair[1]) > 0:
            print(pair[0])
            print(*pair[1])
