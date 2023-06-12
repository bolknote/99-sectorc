import sys
from collections import Counter
data = Counter(x for x in ''.join(sys.stdin.readlines()) if x > '9' or x < '0')
list = data.items()
list.sort(reverse = True, key = lambda x: x[1])

print(repr(data) + "\n")

shift = 1
for (n, (v, q)) in enumerate(list):
    if n == 0xF:
        shift = 2
    else:
        pos = (n + shift) * 256 + ord(v)

        print("x = {}; x();".format(pos))
