def add(l):
    t = 0
    for i in l:
        t += int(i)
    return t


def minus(l):
    t = 2 * int(l[0])
    for i in l:
        t -= int(i)
    return t


def main(l):
    l = l.split('+')
    n=0
    for i in l:
        l[n] = minus(i.split('-'))
        n += 1
    out = add(l)
    print(out)
    return out


text = input('text')
main(text)
