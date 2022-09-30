def fib_count(months, litter):
    """
    Returns the expected number of offspring assuming
    Fibonacci's growth in pairs of species. Accepts months
    to reporduce and original litter size as arguments
    """
    f1 = 1
    f2 = 1
    if months <= 2:
        return 1
    for i in range(months-2):
        f = f1 + f2 * litter
        f2 = f1
        f1 = f
    return f


def fib_death(months, lifespan, litter=1):
    """
    Returns the expected number of offspring given a ceratain time
    and lifespan of the species.
    Follows Finacci's pair growth.
    """
    # make representation of population, rightmost will die in next generation
    pop = [litter]+[0]*(lifespan-1)
    for i in range(months-1):
        newborn = sum(pop[1:])
        pop.insert(0, newborn)
        pop.pop()
    return sum(pop)


if __name__ == '__main__':
    # file = open('files/rosalind_fib.txt')
    # lis = file.read().split(' ')
    # lis = [int(x) for x in lis]
    # print(fib_count(lis[0], lis[1]))
    file = open('files/rosalind_fibd.txt')
    lis = file.read().split(' ')
    lis = [int(x) for x in lis]
    print(fib_death(lis[0], lis[1]))
