from numpy import *
import LGMRES

import sys

if len(sys.argv)<2:
    print 'Usage: python test.py SIZE'
    quit()

n=int(sys.argv[1])


random.seed(55)

A=random.randn(n,n)
b=random.randn(n)
eps=random.randn(n)

x=linalg.solve(A,b)
print x
x0=x+0.1*eps
print x0
x1=LGMRES.solve(A,b,x0=x0)
print x1
print linalg.norm(x1-x)

