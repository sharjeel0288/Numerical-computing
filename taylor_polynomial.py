import math
N = 5  # Significant Number

# True Value of the function
tv = input('equation: ')
val=input('enter value of x : ')
res = ""
eq = tv
if 'exp(x)' in eq:
    eq = eq.replace('exp(x)', str(math.exp(val)))
if 'log(x)' in eq:
     eq = eq.replace('log(x)', str(math.log(val)))
if 'cos(x)' in eq:
        eq = eq.replace('cos(x)', str(math.cos(val)))
if 'sin(x)' in eq:
        eq = eq.replace('sin(x)', str(math.sin(val)))
if 'exp(-x)' in eq:
        eq = eq.replace('exp(-x)', str(math.exp(-val)))
if 'log(-x)' in eq:
        eq = eq.replace('log(-x)', str(math.log(-val)))
if 'sin(-x)' in eq:
        eq = eq.replace('sin(-x)', str(math.sin(-val)))

for element in eq:
        if(element == "x"):
            res += str(val)
        else:

            res += element
            
tv=res
print("True value: \n{}".format(tv))

# Tolerance of the system - Iteration continue until Tolerance error is neglectable for our algorithm.-
eps = 0.5*(10)**(2-N)
print("Tolerance:\n{}".format(eps))
