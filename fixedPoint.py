import math

def fixed_point_iteration(eq, p, TOL):
    error = 1
    iterations = 0
    while error > TOL:
        f=eq
        if 'exp(x)' in f:
         f = f.replace('exp(x)' , str(math.expf(p)))
        if 'log(x)' in f:
            f = f.replace('log(x)' , str(math.log(p)))
        if 'cos(x)' in f:
            f = f.replace('cos(x)' , str(math.cos(p)))
        if 'sin(x)' in f:
            f = f.replace('sin(x)' , str(math.sin(p)))
        if 'exp(-x)' in f:
            f = f.replace('exp(-x)' , str(math.exp(-p)))
        if 'log(-x)' in f:
            f = f.replace('log(-x)' , str(math.log(-p)))
        if 'sin(-x)' in f:
            f = f.replace('sin(-x)' , str(math.sin(-p)))
        if 'x' in f:
            f = f.replace('x' , str(p))
        p_new = (eval(f))
        error = abs(p_new - p)
        p = p_new
        iterations += 1
        print(f'p{iterations} = {p: 0.5f}')
    print(f'Root: {p: 0.5f}\nIterations: {iterations}')

if __name__ == '__main__':
    f = input('Enter equation : ')
    x=float(input("Enter X0 : "))
    fixed_point_iteration(f, x, 1e-5)