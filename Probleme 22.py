def solve(n=0):
    f = open("p022_names.txt", "r")
    texte=f.read()
    Nieme=0
    S=0
    Val=0
    texte=texte[1:len(texte)-1]
    T=sorted(texte.split('","'),key=str)
    for k in T:
        Nieme+=1
        for i in k:
            Val+=ord(i)-64
        S+=Val*Nieme
        Val=0
    return S