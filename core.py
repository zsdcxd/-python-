import logging
from functools import reduce, wraps

logging.basicConfig(level=logging.DEBUG)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug('call %s(%s): ' % (func.__name__, args))
        return func(*args, **kwargs)

    return wrapper


# ################################################################################################################################################################################################################################
#
# 你们怎么一个劲长个子
#                 ,___.、
#               |||————||//|
#               丨눈  눈 |||
#                乀  -  丿


class method(object):

    def __init__(self, alg, a='a', b='b', quickalg=None):
        self.alg = quickalg or alg
        self.a = a
        self.b = b

    def f(self, l):
        return reduce(eval('lambda %s, %s: %s' % (self.a, self.b, self.alg)), [int(i) if bool(i) else 0 for i in l])

    def splt(self, l):
        symbol = ''.join(self.alg.split(self.a))
        symbol = ''.join(symbol.split(self.b))
        lsplited = l.split(symbol)
        for i in lsplited:
            yield i


add = method('a+b')
minus = method('a-b')
multiply = method('a*b')
divide = method('a/b')


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
        ldoubleminus = []
        for tobdoubleminused in tobadded.split('--'):
            lminus = []
            for tobminused in minus.splt(tobdoubleminused):
                lmultiply = []
                for tobmultiolied in multiply.splt(tobminused):
                    ldivide = []
                    for tobdivided in divide.splt(tobmultiolied):
                        ldivide.append(tobdivided)
                    lmultiply.append(divide.f(ldivide))
                lminus.append(multiply.f(lmultiply))
            ldoubleminus.append(minus.f(lminus))
        ladd.append(add.f(ldoubleminus))
    out = str(add.f(ladd))
    logging.info('out:%s' % out)
    return out


# test = input('test') or '(1-2)*(2+3-(2-1))/4'
# core(test)
