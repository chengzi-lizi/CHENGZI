# coding=utf-8

from __future__ import division
import math

def solve_equation(a,b,c):
    delta = b*b - 4*a*c
    if delta<0:
        return False
    elif delta==0:
        return -(b/(2*a))
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta)/(2*a)
        x2 = (-b - sqrt_delta)/(2*a)
        return x1, x2

a,b,c = input("请输入一元二次方程的各项系数： _x^2 + _x + _ = 0\n")

roots = solve_equation(int(a),int(b),int(c))
if roots:
    print("方程的根是:",roots)
else:
    print("此方程无解.")
