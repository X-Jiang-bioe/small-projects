"""
Solution to Enumerating Gene Orders problem

In essense, the resulting permutations from n is placing n
in every position within permutations of n-1
"""


def get_permutations(num):
    '''
    Recursively yields every permutation of list [1,...,n]
    '''
    if num == 1:
        yield [1]
    else:
        for perm in get_permutations(num-1):
            for pos in range(len(perm)+1):
                lis = perm.copy()
                lis.insert(pos, num)
                yield lis


if __name__ == '__main__':
    # its ridiculous to open a file with a single number, but lets stick
    # to the format I established
    with open('files/rosalind_perm.txt') as s:
        ans = tuple(get_permutations(int(s.read())))
        print(len(ans))
        for lis in ans:
            print(*lis)
