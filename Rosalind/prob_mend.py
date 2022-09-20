def prob_mend(k, m, n):
    '''
    Derived f-la using event trees
    '''
    z = k+m+n
    num = k*(k+m+n-1) + m*(k+0.75*(m-1) + 0.5 * n) + n*(k + 0.5 * m)
    den = z*(z-1)
    return num/den


if __name__ == '__main__':
    f = open('files/rosalind_iprb.txt')
    lis = f.read().split(' ')
    lis = [int(x) for x in lis]
    print(prob_mend(lis[0], lis[1], lis[2]))
