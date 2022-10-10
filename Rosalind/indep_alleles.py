import math


def get_prob_het(k, N):
    '''
    In a case where AaBb specimen is 0th generation and
    every mate is AaBb, calculates the probability that at least N
    Aa Bb organisms will belong to the k-th generation of family tree
    (Aa Bb mates at each level not counted).

    Assuming that Mendel's second law holds for the factors.
    '''

    # probability of single sucess
    prob = 1/4.0
    # total number of offspring in generation
    total = 2**k
    tot_prob = 0
    for i in range(0, N):
        p = get_comb(total, i) * (prob**i) * ((1-prob)**(total-i))
        tot_prob += p
    return 1-tot_prob


def get_comb(n, x):
    num = math.factorial(n)
    den = math.factorial(n-x) * math.factorial(x)
    return num/den


if __name__ == '__main__':
    file = open('files/rosalind_lia.txt')
    lis = file.read().split(' ')
    lis = [int(x) for x in lis]
    print(get_prob_het(lis[0], lis[1]))
