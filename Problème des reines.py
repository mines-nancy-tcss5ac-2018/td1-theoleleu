def estlibre(t,ligne,colonne):#On vérifie que si une reine est en placée en [ligne,colonne] elle ne pourrait être capturée
	ok=True
	l,c=1,0
	while ok and l<= ligne:
		c=t[l-1]
		if (ligne-l)==abs(colonne-c):
			ok=False
		l+=1
	return ok



def afficher(l,n,compt):#On fait une fonction d'affichage qui s'adapte si l'échiquier est de taille supérieure à 9 pour garder les colonnes alignées
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


def placer(ligne,n,r,t,compt=0):#On applique une procédure récursive qui va tenter d'effectuer tous les placements possibles en ajoutant 
	#reine par reine quand cela est possible selon la procédure estlibre çi-dessus
	if ligne > n: #On a un compteur(compt qui dénombre les solutions
		afficher(t,n,compt)
		compt+=1
	else:
		colonne=1
		while colonne <= n:
			if r[colonne-1]==0 and estlibre(t,ligne,colonne):#On vérifie que le placement suivant est possible (on vérifie qu'il n'y a pas déjà de reine dans la colonne pour gagner du temps.)
				t[ligne-1]=colonne
				r[colonne-1]= 1#On tente la placement de la reine puisque le placement est possible
				compt=placer(ligne+1,n,r,t,compt)
				r[colonne-1]= 0#Le programme est terminé soit echec soit affichage on peut donc retenter une autre possiblité.
				t[ligne-1]= 0
			colonne+=1
	return compt #On garde la variable non mutable compt r et t sont mutables rien ne sert de les garder ici
			
def solve(n):#Fonction solution
	t=[0]*n#On crée un échiquier numéro de colonne
	r=[0]*n#On crée un échiquier numéro de ligne
	compt=placer(1,n,r,t)#On lance l'algorithme
	print("Il y a ",compt,"solutions au problème des",n,"reines.")#On affiche le nombre de solutions.
