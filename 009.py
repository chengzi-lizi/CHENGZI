# coding=utf-8

def josephus(n,k):
    loop = [number for number in (range(1,n+1))]
    a = 0
    while True:
        b = loop.pop(0)
        a += 1
        if a == k:
            a = 0
            continue
        loop.append(b)
        if len(loop) == int(k-1):
            print(loop)
            break

josephus(50,3)

