def fib_count(months, litter):
    f1 = 1
    f2 = 1
    if months <= 2:
        return 1
    for i in range(months-2):
        f = f1 + f2 * litter
        f2 = f1
        f1 = f
    return f


if __name__ == '__main__':
    file = open('files/rosalind_fib.txt')
    lis = file.read().split(' ')
    lis = [int(x) for x in lis]
    print(fib_count(lis[0], lis[1]))
