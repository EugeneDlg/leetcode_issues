from math import sqrt

from utils import verify_func


N = int(input("input a number: "))


def fact1(N):
    sq_n = int(sqrt(N))
    q = N
    mult = 1
    lst = []
    for a in range(2,sq_n+1):
        if a > int(sqrt(q))+1: break
        while(q%a==0):
            mult *= a
            lst.append(a)
            q /= a
    q0 = int(N/mult)
    if q0 > 1: lst.append(q0)
    print(lst)


def fact0(N):
    i = 2
    q = N
    mult = 1
    lst = []
    while(i < int(sqrt(q)) + 1):
        while(q % i == 0):
            q /= i
            mult *= i
            lst.append(i)
        i += 1
    q0 = int(N/mult)
    if q0 > 1: lst.append(q0)
    print(lst)


verify_func(fact0, N)
verify_func(fact1, N)

