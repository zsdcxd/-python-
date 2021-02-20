import logging
from functools import reduce, wraps
from math import sin, cos, tan, asin, acos, atan, pi, sinh, cosh, tanh, asinh, acosh, atanh

logging.basicConfig(level=logging.DEBUG)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug('call %s%s: ' % (func.__name__, args))
        return func(*args, **kwargs)

    return wrapper


# ######################################################################################################################
#
# 你们怎么一个劲长个子
#              ,,___.、
#         ／   ||———|/||(((ヽ
#        (　 ﾉ　丨눈  눈| ￣Ｙ＼
#        |　(＼　乀 -  丿  ｜  )
#         ヽ　ヽ`  _     ノ  /
# 　        ＼ |　⌒Ｙ⌒　/  /
# 　         ｜ヽ · ｜ ·  ﾉ/
#           ｜＼トー仝ーイ /
# 　　       ｜   ミ土彡  /
#            )\    °   /
#            (  \  y   \
#           /    /   \ \\
#          / /  /     \  \
#         ( (  ).      ) ).)
#        (    ).        (| |
#        |   /           \ |
#      nn.   ).          （. nn.


class basicf(object):

    def __init__(self, alg, symbol, times=0, tobname=None):
        if '(' in alg:
            variable = alg.split('(')[1].split(')')[0]
        else:
            variable = ','.join(alg.split(symbol[0]))
        self.alg = alg
        self.variable = variable
        self.times = times
        self.symbol = symbol
        self.tobname = tobname

    def f(self, l):
        variable = self.variable
        if not self.tobname:
            out = reduce(eval('lambda %s: %s' % (variable, self.alg)),
                         [eval(i) if bool(i) else self.times for i in l])
            return str(out)
        else:
            f = eval('lambda %s: %s' % (variable, self.alg))
            out = f(eval(l))
            return str(out)

    def splt(self, l):
        symbollist = self.symbol
        n = len(symbollist)
        t = 0
        splittedlist = [l]
        while t < n:
            s = []
            symbol = symbollist[t]
            for i in splittedlist:
                if symbol in i:
                    s += i.split(symbol)
                    splittedlist = s
            t += 1
        # while '' in splittedlist:
        #     splittedlist.remove('')
        return splittedlist

    def onevariableq(self, x):
        for symbol in self.symbol:
            if symbol in x:
                for tobdone in self.splt(x):
                    if bool(tobdone):
                        logging.debug('%s:%s,type:%s' % ('tob' + self.tobname, tobdone, type(tobdone)))
                        x = self.f(tobdone)
                        logging.debug('%s:%s' % (self.tobname, x))
        return x


add = basicf('a+b', ['+', '+'])
minus = basicf('a-b', ['-', '-'])
multiply = basicf('a*b', ['*', '×'])
divide = basicf('a/b', ['/', '÷'])
sqroot = basicf('a**0.5', ['√'], tobname='sqrooted')
power = basicf('a**b', ['**', '^'])
sinc = basicf('sin(a)', ['sin'], tobname='sined')
cosc = basicf('cos(a)', ['cos'], tobname='cosed')
tanc = basicf('tan(a)', ['tan'], tobname='taned')
asinc = basicf('asin(a)', ['asin', 'arcsin'], tobname='arcsined')
acosc = basicf('acos(a)', ['acos', 'arccos', 'arcos'], tobname='arccosed')
atanc = basicf('atan(a)', ['atan', 'arctan'], tobname='arctaned')
sinhc = basicf('sinh(a)', ['sinh'], tobname='sinhed')
coshc = basicf('cosh(a)', ['cosh'], tobname='coshed')
tanhc = basicf('tanh(a)', ['tanh'], tobname='tanhed')
asinhc = basicf('asinh(a)', ['asinh', 'arcsinh'], tobname='arcsinhed')
acoshc = basicf('acosh(a)', ['acosh', 'arccosh', 'arcosh'], tobname='arccoshed')
atanhc = basicf('atanh(a)', ['atanh', 'arctanh'], tobname='arctanhed')


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
    logging.debug('l:%s,start:%s,end:%s' % (l, start, end))
    if start + end >= 0:
        if '(' in l[end:] or '（' in l[end:]:
            return str(core(l[: start] + str(eval(core(l[start + 1: end]))) + l[end + 1:]))
        else:
            return l[: start] + str(eval(core(l[start + 1: end]))) + l[end + 1:]
    else:
        return str(l)


changevariableqtimes = 0


@log
def core(l='0'):
    global changevariableqtimes

    def onevariableq(x):
        x = sqroot.onevariableq(x)
        x = sinc.onevariableq(x)
        x = cosc.onevariableq(x)
        x = tanc.onevariableq(x)
        x = asinc.onevariableq(x)
        x = acosc.onevariableq(x)
        x = atanc.onevariableq(x)
        x = sinhc.onevariableq(x)
        x = coshc.onevariableq(x)
        x = tanhc.onevariableq(x)
        x = asinhc.onevariableq(x)
        x = acoshc.onevariableq(x)
        x = atanhc.onevariableq(x)
        return x

    def changevariableq(x):
        if '**' in x:
            x = '^'.join(x.split('**'))
        if '--' in x:
            x = '+'.join(x.split('--'))
        if '[' or ']' in x:
            x = '('.join(x.split(('[')))
            x = ')'.join((x.split(']')))
        if '{' or '}' in x:
            x = '('.join(x.split('{'))
            x = ')'.join((x.split('}')))
        logging.debug('chanded:%s' % (x))
        return x

    while changevariableqtimes == 0:
        l = changevariableq(l)
        changevariableqtimes += 1
    l = brackets(l)
    logging.info('brackets(l):%s' % l)
    ladd = []
    for tobadded in add.splt(l):
        logging.debug('tobadded:%s' % tobadded)
        lminus = []
        for tobminused in minus.splt(tobadded):
            logging.debug('tobminused:%s' % tobminused)
            ldivide = []
            for tobdivided in divide.splt(tobminused):
                logging.debug('tobdivided:%s' % tobdivided)
                lmultiply = []
                for tobmultiplied in multiply.splt(tobdivided):
                    logging.debug('tobmultiplied:%s' % tobmultiplied)
                    lpower = []
                    for tobpowered in power.splt(tobmultiplied):
                        logging.debug('tobpowered:%s' % tobpowered)
                        tobpowered = onevariableq(tobpowered)
                        lpower.append(tobpowered)
                    logging.debug('lpower:%s' % lpower)
                    lmultiply.append(power.f(lpower))
                logging.debug('lmultiply:%s' % lmultiply)
                ldivide.append(multiply.f(lmultiply))
            logging.debug('ldivide:%s' % ldivide)
            lminus.append(divide.f(ldivide))
        logging.debug('lminus:%s' % lminus)
        ladd.append(minus.f(lminus))
    logging.debug('ladd:%s' % ladd)
    out = add.f(ladd)
    logging.debug('out:%s' % out)
    return out


test = input('test') or '0'
core(test)
