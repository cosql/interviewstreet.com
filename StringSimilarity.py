import os

def main():
    t = int(raw_input());
    for case in range(t):
        a = raw_input()
        res = len(a)
        more = 0
        c = []
        for i in range(1, res):
            if (a[i] == a[0]):
                more += 1
                c.append(i)
        res += more
        k = 1
        while (1):
            if (more == 0):
                break
            d = []
            more = 0
            for i in range(len(c)):
                if c[i] + 1 < len(a):
                    if (a[c[i] + 1] == a[k]):
                        more += 1
                        d.append(c[i] + 1)
            c = d
            res += more
            k += 1
        print res


if __name__ == '__main__':
    main()
