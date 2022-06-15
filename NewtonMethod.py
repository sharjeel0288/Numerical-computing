import math
from sympy import *
import time
import sympy as sym


def f(val):
    res = ""
    eq=equation
    if 'exp(x)' in eq:
        eq = eq.replace('exp(x)' , str(math.exp(val)))
    if 'log(x)' in eq:
        eq = eq.replace('log(x)' , str(math.log(val)))
    if 'cos(x)' in eq:
        eq = eq.replace('cos(x)' , str(math.cos(val)))
    if 'sin(x)' in eq:
        eq = eq.replace('sin(x)' , str(math.sin(val)))
    if 'exp(-x)' in eq:
        eq = eq.replace('exp(-x)' , str(math.exp(-val)))
    if 'log(-x)' in eq:
        eq = eq.replace('log(-x)' , str(math.log(-val)))
    if 'sin(-x)' in eq:
        eq = eq.replace('sin(-x)' , str(math.sin(-val)))

    for element in eq:
        if(element=="x"):
            res+=str(val)
        else:
        
            res+=element
    return (eval(res))

def f_dif(val):
    derivative = sym.diff(equation)
    res = ""
    eq=str(derivative)
    if 'exp(x)' in eq:
        eq = eq.replace('exp(x)' , str(math.exp(val)))
    if 'log(x)' in eq:
        eq = eq.replace('log(x)' , str(math.log(val)))
    if 'cos(x)' in eq:
        eq = eq.replace('cos(x)' , str(math.cos(val)))
    if 'sin(x)' in eq:
        eq = eq.replace('sin(x)' , str(math.sin(val)))
    if 'exp(-x)' in eq:
        eq = eq.replace('exp(-x)' , str(math.exp(-val)))
    if 'log(-x)' in eq:
        eq = eq.replace('log(-x)' , str(math.log(-val)))
    if 'sin(-x)' in eq:
        eq = eq.replace('sin(-x)' , str(math.sin(-val)))

    for element in eq:
        if(element=="x"):
            res+=str(val)
        else:
        
            res+=element
    return (eval(res))
     

if __name__ == '__main__':
    equation = input('Enter equation : ')
    x=float(input("Enter X0 : "))
    last=float(0)
    i=1
    print('p0 = ',x)
    while (last!=x):
        last=x      
        x=last-(f(last)/f_dif(last))
        print(f'p{i} = {x: 0.5f}')
        i=i+1
        
    print(f'Root: {last: 0.5f}\nIterations: {i}')
        
        
        