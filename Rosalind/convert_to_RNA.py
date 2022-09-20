def convert_to_RNA(s):
    return s.replace('T', 'U')


if __name__ == '__main__':
    f = open('files/rosalind_rna.txt')
    print(convert_to_RNA(f.read()))
