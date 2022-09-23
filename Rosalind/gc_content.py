import count_nt
import parse_fasta


def gc_content(file):
    """
    Returns gc-content info given fasta file
    """
    d = parse_fasta.parse_fasta(file)
    keys = list(d.keys())
    vals = list(map(gc_from_seq, d.values()))
    new_dic = {keys[i]: vals[i] for i in range(len(vals))}
    return new_dic


def get_mac_gc(dic):
    m = max(dic, key=dic.get)
    return m


def gc_from_seq(seq):
    counts = count_nt.count_nt(seq)
    return (counts[1] + counts[2])/sum(counts) * 100


if __name__ == "__main__":
    dic = gc_content('files/rosalind_gc.txt')
    m = get_mac_gc(dic)
    print(m+"\n"+str(dic[m]))
