import logging
from functools import reduce, wraps
from math import sin, cos, tan, asin, acos, atan

logging.basicConfig(level=logging.DEBUG)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug('call %s(%s): ' % (func.__name__, args))
        return func(*args, **kwargs)

    return wrapper


# ######################################################################################################################
#
# 你们怎么一个劲长个子
#               ,___.、
#             |||————||//|
#             丨눈  눈 |||
#              乀  -  丿
#         ／            (((ヽ
#        (　 ﾉ　　 　　 ￣Ｙ＼
#        |　(＼　         ｜    )
#         ヽ　ヽ`  _     ノ    /
# 　         ＼ |　⌒Ｙ⌒　/  /
# 　        ｜ヽ   · ｜  ·  ﾉ/
#          　｜＼トー仝ーイ  /
# 　　       ｜    ミ土彡  /
#           ) \     °   /
#          (   \   y     \
#          /     /  \ \   \
#        /  /   /      \
#       ( (    ).       ) ).  )
#      (      ).         ( |  |
#       |    /            \   |
#     nn.   ).             （. nn.


class basicf(object):

    def __init__(self, alg, symbol, times, a='a', b='b', quickalg=None):
        self.alg = quickalg or alg
        self.a = a
        self.b = b
        self.times = times
        self.symbol = symbol

    def f(self, l):
        variable = self.a
        if self.b in self.alg:
            variable += ','
            variable += self.b
            return reduce(eval('lambda %s: %s' % (variable, self.alg)), [int(i) if bool(i) else self.times for i in l])
        elif l:
            out = list(
                map(eval('lambda %s: %s' % (variable, self.alg)), [int(i) if bool(i) else self.times for i in l]))
            return out[0]

    def splt(self, l):
        symbollist = self.symbol
        n = len(symbollist)
        t = 0
        splittedlist = [l]
        while t < n:
            s = []
            symbol = symbollist[t]
            for i in splittedlist:
                s += i.split(symbol)
            splittedlist = s
            t += 1
        return splittedlist


class trigf(object):

    def __init__(self, alg, a='x'):
        self.alg = alg
        self.a = a

    def f(self, l):
        pass


add = basicf('a+b', ['+', '+'], 0)
minus = basicf('a-b', ['-', '-'], 0)
multiply = basicf('a*b', ['*', '×'], 0)
divide = basicf('a/b', ['/', '÷'], 0)
sqroot = basicf('a**0.5', ['√'], 0)
power = basicf('a**b', ['**', '^'], 0)


@log
def brackets(l):
    start = min(l.find('(') if l.find('(') != -1 and l.find('（') != -1 else max(l.find('('), l.find('（')),
                l.find('（') if l.find('(') != -1 and l.find('（') != -1 else max(l.find('('), l.find('（')))
    n = start
    end = 0
    times = 0
    while n < len(l):
        if l[n] == '(' or l[n] == '（':
            times += 1
        if l[n] == ')' or l[n] == '）':
            times -= 1
            if times == 0:
                end = n
                break
        n += 1
    logging.info('l:%s,start:%s,end:%s' % (l, start, end))
    if start + end >= 0:
        if '(' in l[end:] or '（' in l[end:]:
            return core(l[: start] + core(l[start + 1: end]) + l[end + 1:])
        else:
            return l[: start] + core(l[start + 1: end]) + l[end + 1:]
    else:
        return str(l)


@log
def core(l='0'):
    l = brackets(l)
    logging.info('brackets(l):%s' % l)
    ladd = []
    for tobadded in add.splt(l):
        logging.debug('tobadded:%s' % tobadded)
        ldoubleminus = []
        for tobdoubleminused in tobadded.split('--'):
            logging.debug('tobdoubleminused:%s' % tobdoubleminused)
            lminus = []
            for tobminused in minus.splt(tobdoubleminused):
                logging.debug('tobminused:%s' % tobminused)
                ldivide = []
                for tobdivided in divide.splt(tobminused):
                    logging.debug('tobdivided:%s' % tobdivided)
                    lmultiply = []
                    for tobmultiplied in multiply.splt(tobdivided):
                        logging.debug('tobmultiplied:%s' % tobmultiplied)
                        if '√' in tobmultiplied:
                            for tobsqrooted in sqroot.splt(tobmultiplied):
                                tobmultiplied = sqroot.f(tobsqrooted)
                        lmultiply.append(tobmultiplied)
                    logging.debug('lmultiply:%s' % lmultiply)
                    ldivide.append(multiply.f(lmultiply))
                logging.debug('ldivide:%s' % ldivide)
                lminus.append(divide.f(ldivide))
            logging.debug('lminus:%s' % lminus)
            ldoubleminus.append(minus.f(lminus))
        logging.debug('ldoubleminus:%s' % ldoubleminus)
        ladd.append(add.f(ldoubleminus))
    logging.debug('ladd:%s' % ladd)
    out = str(add.f(ladd))
    logging.debug('out:%s' % out)
    return out

#
# test = input('test') or '(1-2)×(2+3-(2-1))/(√4)'
# core(test)
