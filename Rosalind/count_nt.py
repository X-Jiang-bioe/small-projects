from collections import Counter
letters = ['A', 'C', 'G', 'T']
test = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
def count_bases(s):
    counter = Counter(s)
    print(Counter(letters))