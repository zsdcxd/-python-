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
#               |||—————||//|
#               丨눈   눈 |||
#                乀   -  丿


class method(object):

    def __init__(self, alg, a='a', b='b'):
        self.alg = alg
        self.a = a
        self.b = b

    def f(self, l):
        return reduce(eval('lambda %s, %s: %s' % (self.a, self.b, self.alg)), [int(i) if bool(i) else 0 for i in l])


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
def core(l):
    l = brackets(l)
    logging.info('brackets(l):%s' % l)
    l = l.split('+')
    n1 = 0
    for m in l:
        n2 = 0
        m = m.split(('--'))
        for s in m:
            m[n2] = minus.f(s.split('-'))
            n2 += 1
        l[n1] = add.f(m)
        n1 += 1
    out = str(add.f(l))
    logging.info('out:%s' % out)
    return out
#
# test = input('test') or '0'
# core(test)
