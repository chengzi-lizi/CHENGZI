# coding=utf-8

a, b = 0, 1

for i in range(100):
    a, b = b, a+b

print(a)
