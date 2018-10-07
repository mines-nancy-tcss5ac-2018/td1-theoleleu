def solve(n=1000):
    a=2**n
    S=0
    while a!=0:
        S+=a%10
        a=a//10
    return S