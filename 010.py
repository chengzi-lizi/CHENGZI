# coding=utf-8

def josephus(n,m):
    loop = [number for number in range(1,n+1)]
    key = m-1 
    while True:
        if m < len(loop):
            loop = loop[key+1:] + loop[:key]
        if m == len(loop):
            loop.pop(-1)
            print(loop)
            break

josephus(50,3)
