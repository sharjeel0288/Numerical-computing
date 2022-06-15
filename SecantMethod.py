import math

def secant(f, x1, x2, TOL):
    error = 1
    iterations = 0
    print(f'x0: {x1}\nx1: {x2}')
    while error > TOL:
        
        
        eq1=f
        if 'exp(x)' in eq1:
         eq1 = eq1.replace('exp(x)' , str(math.expf(x1)))
        if 'log(x)' in eq1:
            eq1 = eq1.replace('log(x)' , str(math.log(x1)))
        if 'cos(x)' in eq1:
            eq1 = eq1.replace('cos(x)' , str(math.cos(x1)))
        if 'sin(x)' in eq1:
            eq1 = eq1.replace('sin(x)' , str(math.sin(x1)))
        if 'exp(-x)' in eq1:
            eq1 = eq1.replace('exp(-x)' , str(math.exp(-x1)))
        if 'log(-x)' in eq1:
            eq1 = eq1.replace('log(-x)' , str(math.log(-x1)))
        if 'sin(-x)' in eq1:
            eq1 = eq1.replace('sin(-x)' , str(math.sin(-x1)))
        if 'x' in eq1:
            eq1 = eq1.replace('x' , str(x1))
            
        eq2=f
        
        if 'exp(x)' in eq2:
         eq2 = eq2.replace('exp(x)' , str(math.expf(x2)))
        if 'log(x)' in eq2:
            eq2 = eq2.replace('log(x)' , str(math.log(x2)))
        if 'cos(x)' in eq2:
            eq2 = eq2.replace('cos(x)' , str(math.cos(x2)))
        if 'sin(x)' in eq2:
            eq2 = eq2.replace('sin(x)' , str(math.sin(x2)))
        if 'exp(-x)' in eq2:
            eq2 = eq2.replace('exp(-x)' , str(math.exp(-x2)))
        if 'log(-x)' in eq2:
            eq2 = eq2.replace('log(-x)' , str(math.log(-x2)))
        if 'sin(-x)' in eq2:
            eq2 = eq2.replace('sin(-x)' , str(math.sin(-x2)))
        if 'x' in eq2:
            eq2 = eq2.replace('x' , str(x2))
            
      
        fx1=eval(eq1)
        fx2=eval(eq2)
        x_new = x2 - (fx2*(x2-x1))/(fx2-fx1)
        error = abs(x_new - x2)
        x1 = x2
        x2 = x_new
        iterations += 1
        print(f'x{iterations+1}: {x2: 0.5f}')
    print(f'Result: {x2: 0.5f}\nIterations: {iterations}')

if __name__ == '__main__':
    f = input('Enter equation : ')
    x0=float(input("Enter X0 : "))
    x1=float(input("Enter X1 : "))
    secant(f, x0, x1, 1e-4)