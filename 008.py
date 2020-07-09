# coding=utf-8

import math

def prime_number(n):
    """
    判断一个数是否是素数
    """
    if n <= 1:
        return False
    for i in range(2, int(round(n/2) + 1)):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(0,100) if prime_number(i)]    
print(primes)
