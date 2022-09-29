import parse_fasta
import count_nt
import numpy as np
import re


class CommonAncestor():
    """
    Class used to generate a matrix profile and consensus profile
    given a fasta file

    Attributes
    ----------
    arr: NumPy Array
        4*n array for n sequences
        rows are counts of A, C, G, T respectively
    """
    def __init__(self, fasta) -> None:
        super().__init__()
        self.keys = ["A", "C", "G", "T"]
        self.arr = self.parse_f(fasta)

    def parse_f(self, fasta):
        reg = re.compile("(\/+.*)+")
        # if is path to file
        if reg.search(fasta):
            return self._parse_f(parse_fasta.parse_fasta(fasta))
        else:
            return self._parse_f(parse_fasta.parse_fasta_string(fasta))

    def _parse_f(self, fasta_dic):
        # transposing the list of actual sequences to count number of
        # nucleotides in each column
        pseudo_seq = [''.join(s) for s in zip(*fasta_dic.values())]
        counts = [count_nt.count_nt(seq) for seq in pseudo_seq]
        arr = np.array(counts).transpose()
        return arr

    def consensus(self):
        """
        Returns the consensus string of the fasta file
        in cases of multiple possibilities, gives priority
        in following order: A, C, G, T
        """
        loc = np.argmax(self.arr, axis=0)
        return "".join([self.keys[i] for i in loc])

    def profile(self):
        """
        Returns the profile matrix in dictionary form
        given the array of sequences

        Returns
        -------
        dic: dictionary
            {nucleotide: [number of nt in sequence]}
        """
        dic = {}
        for key, value in zip(self.keys, self.arr):
            dic[key] = list(value)
        return dic


if __name__ == "__main__":
    test = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT"""
    test2 = "files/rosalind_cons.txt"
    ca = CommonAncestor(test2)
    print(ca.consensus())
    prof = ca.profile()
    for key in prof:
        print(key+':', end=' ')
        print(*prof[key])
