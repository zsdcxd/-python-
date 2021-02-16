def add(l):
    t = 0
    for i in l:
        t += int(i)
    return t


def minus(l):
    t = 0
    for i in l:
        t -= i
    return int(i)


def main(l):
    l = l.split('+')
    out = add(l)
    print(out)
    return out


text = input('text')
main(text)
