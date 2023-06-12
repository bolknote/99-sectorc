print("Enter your phrase: ", end = '')
input = input()
print("Output: \n")

from itertools import *
t0 = [' ', 'e', 'o', 't', 'l', 'b', 'n', 'a', 's', 'r', 'f', 'w', '\n', 'd']
t1 = ['h', ',', '.', 'u', 'T', 'i', 'k', 'p', 'm', 'G', 'N', 'y']

def conv(ch):
    try:
        yield t0.index(ch) + 1
    except ValueError:
        yield 15
        yield t1.index(ch) + 1


def make_shifter():
    pos = 0
    gr  = 0

    def shifter(v):
        nonlocal pos
        nonlocal gr

        if pos == 4:
            pos = 0
            gr += 1

        if pos == 3 and v == 0xF:
            pos = 1
            gr += 1
            ret = (v, gr, )
        else:
            ret = (v, gr, )
            pos += 1

        return ret
    return shifter

shifter = make_shifter()

gen = (shifter(x) for x in chain(*(conv(ch) for ch in input)))
gen = groupby(gen, key = lambda x: x[1])

for x in gen:
    sum = 0
    for y in list(x[1])[::-1]:
        sum *= 16
        sum += y[0]

    print("s = {}; ps(); ".format(sum))

