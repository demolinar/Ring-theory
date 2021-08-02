from sympy import *
import numpy as np

x = symbols("x")
def solution(ecuation, z_n):
    '''
    Solve equations in Zn with one variable

    '''
    for i in range(z_n):
        solutions = ecuation.subs(x, i)
        if (solutions % z_n == 0):
            print(i, "with", solutions)


solution((x-1)**2*(x+1)**2, 3)
# solution(x**2 + 2*x + 2 , 6)
# solution(5*x-2, 13)




