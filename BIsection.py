import math
from sympy import symbols, solve
equation = input('equation: ')

a=float(input("Enter a: "))
b=float(input("Enter b: "))
tolbase=float(input('Enter tolerance base (0 for unknown) : '))
tolpow=float(input('Enter tolerance power (0 for unknown) : '))
i=0
last=0
c=0
iter=float(input("Enter number of iterations (0 for unknown) : "))
c=0




def f(val, Equ):
    res = ""
    eq=Equ
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
    return truncate(eval(res),4)


def cal_c(a,b):
   return ((a+b)/2)

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper
    
if(tolbase!=0 and tolpow!=0):
    N = symbols('N')
    tolEq=2**-N-tolbase**tolpow
    iteration = (solve(tolEq))
    iter=iteration.pop(0)
    iter = math.ceil(iter)
    print('Number of iterations : ',iter)

while 1:
    last=c
    c=truncate(cal_c(a,b),4)
    print(" {:<0} {:<8} {:<0} {:<8} {:<0} {:<0} {:<8} {:<0}  {:<8} {:<0} {:<8} {:<0} {:<8}".format("a : ",a,"\tb : ",b,"\tP"+str(i)," : " ,c, "\tF(p) : ",f(c,equation) ,"\t\tF(a) : ",f(a,equation),"\tF(b) : ",f(b,equation)))
    # print(f(a)*f(c))
    if(last==c):
        break
    if(f(c,equation)==0):
        
        break
    if(f(c,equation)*f(a,equation)>0):
        a=c
    if(f(c,equation)*f(a,equation)<0):
        b=c
    if(i==iter and iter!=0):
        break
    i+=1

print("RESULT : ",c)



