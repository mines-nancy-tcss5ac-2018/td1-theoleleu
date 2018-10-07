def est_palindrome(num):
     a=str(num)
     return a==a[::-1]

def palindrome(num):
     return int(str(num)[::-1])


def Lychrel(num):
    i,a=0,num
    est_lychrel=True
    while est_lychrel and i<=50:
        a+=palindrome(a)
        if est_palindrome(a):
             est_lychrel=False
        i+=1 
    return est_lychrel



def solve(n=10000):
    S=0
    for k in range(n):
        if Lychrel(k):
            S+=1
    return S