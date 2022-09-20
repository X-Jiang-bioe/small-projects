dic = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def reverse_compliment(s):
    lis = list(s)
    out = [dic[x] for x in lis]
    out.reverse()
    return(''.join(out))


if __name__ == '__main__':
    f = open('files/rosalind_revc.txt')
    print(reverse_compliment(f.read()))
