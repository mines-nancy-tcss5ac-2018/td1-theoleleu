def solve(n=1000):
    puissance=2**n
    S=0
    while puissance!=0:
        S+=puissance%10
        puissance=puissance//10
    return S
