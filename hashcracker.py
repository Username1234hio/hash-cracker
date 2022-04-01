import math
import matplotlib as pt
from matplotlib import pyplot as plt
import random as rn
import numpy as np
s = input()
print('trying to find code' + s)
for x in range(15792090000000000000000000000000000000000000000000000000000000000000000000):
  a = 0
  b = 1
  c = 2
  d = 3
  e = 4
  f = 5
  g = 6
  h = 7
  i = 8
  j = 9
  k = 'a'
  l = 'b'
  m = 'c'
  n = 'd'
  o = 'e'
  p = 'f'
  l = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
  k = []
  for x in range(64):
    n = rn.choice(l)
    k.append(n)
  z = str(k)
  zz = z.translate({ord(","):None})
  zzz = zz.translate({ord("["):None})
  zzzz = zzz.translate({ord("]"):None})
  zzzzz = zzzz.translate({ord(","):None})
  zzzzzz = zzzzz.translate({ord("'"):None})
  zzzzzzz = zzzzzz.translate({ord(" "):None})
  print(zzzzzzz)
  if zzzzzzz == s:
    print(solved)
