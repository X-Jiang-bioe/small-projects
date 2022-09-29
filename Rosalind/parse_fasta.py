import re


def parse_fasta(fasta_file):
    """
    Reads the .fasta file given its location
    returns a dictionary: {fasta name: sequence}
    """
    with open(fasta_file) as file:
        return parse_fasta_string(file.read())


def parse_fasta_string(fasta):
    """
    Given a FASTA string returns dictionary with
    key: sequence name and value: sequence
    """
    d = {}
    items = re.split("(>.*)", fasta)[1:]
    for i in range(0, len(items), 2):
        d[items[i][1:]] = items[i+1].replace("\n", "")
    return d


if __name__ == "__main__":
    test = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

    # print(parse_fasta_string(test))
    print(parse_fasta('files/rosalind_gc.txt'))
