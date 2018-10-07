def estlibre(t,ligne,colonne):
	ok=True
	l,c=1,0
	while ok and l<= ligne:
		c=t[l-1]
		if (ligne-l)==abs(colonne-c):
			ok=False
		l+=1
	return ok



def afficher(l,n,compt):
	compt+=1
	print("Solution n°",compt)
	for k in range(n):
		print(k+1,end='')
		if k<9:
			print(" ",end='')
		print(" ",end='')
		for i in range(1,n+1):
			if i==l[k]:
				print("x  ",end='')
			else:
				print("o  ",end='')
		print("")
	print("   ",end='')
	for k in range(n):
		print(k+1,end='')
		if k<9 :
			print(" ",end='')
		print(" ",end='')
	print("")


def placer(ligne,n,r,t,compt=0):
	if ligne > n:
		afficher(t,n,compt)
		compt+=1
	else:
		colonne=1
		while colonne <= n:
			if r[colonne-1]==0 and estlibre(t,ligne,colonne):
				t[ligne-1]=colonne
				r[colonne-1]= 1
				compt,r,t=placer(ligne+1,n,r,t,compt)
				r[colonne-1]= 0
				t[ligne-1]= 0
			colonne+=1
	return compt,r,t
			
def solve(n):
	t=[0]*n
	r=[0]*n
	compt,r,t=placer(1,n,r,t)
	print("Il y a ",compt,"solutions au problème des",n,"reines.")