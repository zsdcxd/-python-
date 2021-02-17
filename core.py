import functools
import logging
from functools import reduce

logging.basicConfig(level=logging.DEBUG)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug('call %s(%s): ' % (func.__name__, args))
        return func(*args, **kwargs)
    return wrapper


def add(l):
    return sum([int(i) if bool(i) else 0 for i in l])


def minus_f(a=0, b=0):
    return a - b


def minus(l):
    return reduce(minus_f, [int(i) if bool(i) else 0 for i in l])


def multiply_f(a=0, b=0):
    return a * b


def multiply(l):
    return reduce(minus_f, [int(i) for i in l])


def divide_f(a, b):
    return a / b


def divide(l):
    return reduce(divide_f, [int(i) for i in l])


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
        return l


@log
def core(l):
    l = brackets(l)
    logging.info('brackets(l):%s' % l)
    l = l.split('+')
    n = 0
    for m in l:
        l[n] = minus(m.split('-'))
        n += 1
    out = str(add(l))
    logging.info('out:%s' % out)
    return out


test = input('test') or '1-（（1+2-3）-（1-2）+1-（2+1））'
core(test)

