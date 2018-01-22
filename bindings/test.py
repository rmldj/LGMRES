from __future__ import print_function
from numpy import *
import LGMRES

import sys

if len(sys.argv)<2:
    print('Usage: python test.py SIZE')
    quit()

n=int(sys.argv[1])


random.seed(55)

A=random.randn(n,n)
b=random.randn(n)
eps=random.randn(n)

x=linalg.solve(A,b)
print('linalg.solve solution',x,'\n')
x0=x+0.1*eps
print('initial guess',x0,'\n')
x1=LGMRES.solve(A,b,x0=x0)
print('LGMRES.solve solution',x1,'\n')
print('norm of the difference',linalg.norm(x1-x))

