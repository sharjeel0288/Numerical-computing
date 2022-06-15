from sympy import *
 # We have to create a "symbol" called x
from typing import get_type_hints
x=symbols('x')
f = (input("eq : "))
eq=f
res = 1
for element in eq:
    if(element=="x"):
        res+=x
    else:
        res+=int(element)
    print(res)
print(f(3))
f_prime = f.diff(x)
print(f)
print(f_prime)