# pair otcomes table
dic = {1: 1, 2: 1, 3: 1, 4: .75, 5: .5, 6: 0}


def exp_offspring(pop):
    """
    Returns the number of expected offspring
    displaying the dominant phenotype in the next generation,
    under the assumption that every couple has exactly two offspring.
    pop = [AA_pair_num, AAAa_num, ... aa_pair_num]
    """
    ngen = 0
    for i, pair in enumerate(pop):
        # times 2 cause expect 2 offspring
        ngen += 2*pair*dic[i+1]
    return ngen


if __name__ == "__main__":
    # test = [1, 0, 0, 1, 0, 1]
    # print(exp_offspring(test))

    f = open("files/rosalind_iev.txt")
    pop = [int(x) for x in f.read().split(' ')]
    print(exp_offspring(pop))
