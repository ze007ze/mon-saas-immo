import random
#1=sexe , 2=surnom , 3=age , 4=crush
joueur={"sylvio":{"1":'garçon',"2":'ibrahim',"3":18,"4":'beaucoup'},
		"bilal":{"1":'Homme poilue',"2":'gros lardon',"3":18,"4":'beaucoup'},
		"chiara":{"1":'femme en chaleur',"2":'la tana des neiges',"3":18,"4":'thomas'},
		"alexis":{"1":'petit homme',"2":'aleskibidi',"3":17,"4":'beaucoup'},
		"mathys":{"1":'garçon',"2":'le casse couilles',"3":18,"4":'kesya'},
		"alexandre":{"1":'demi homme',"2":'le jeune parfais',"3":16,"4":'eline'},
		"oscar":{"1":'HOMME',"2":"l'aryan","3":18,"4":'clemence'},
		"felix":{"1":'HOMO',"2":'le petit parfais/casse couilles',"3":17,"4":'kesya'},
		"kesya":{"1":'femelle',"2":'la pute asiatique',"3":17,"4":'felix'},}
name=random.randint(1,9)

if name==1:
	name='sylvio'
elif name==2:
	name='bilal'
elif name ==3:
	name='chiara'
elif name==4:
	name='alexis'
elif name==5:
	name= 'mathys'
elif name==6:
	name= 'alexandre'
elif name== 7:
	name='oscar'
elif name==8:
	name='felix'
elif name==9:
	name='kesya'
 

j_choice=[]
nbre=[]
nfl=[1,2,3,4]
for i in range(4):
	choix=random.randint(1,4)
	nbre.append(choix)


for k in range(5):
	for a in range(4):
		if nbre.count(k) > 1:
			nbre.remove(k)
		else:
			continue

for o in range(4):
	for n in range(0,4):
		if nfl[n] not in nbre:
			nbre.append(nfl[n])
		else:
			continue

essai=0	
idea=0
player=list(joueur[name].values())
truc=list(joueur[name])
valeur=list(joueur[name].values())
for j in range (0,4):
	print('____________________________________________________________')
	essai += 1
	if nbre[j]==1:
		if player[j]=='femme en chaleur' or player[j]=='femelle':
			print("cette chienne est une",valeur[nbre[j]-1])
		else:
			print("cette personne est un",valeur[nbre[j]-1])
	elif nbre[j]==2:
		print("le surnom de cet eunuque c'est",valeur[nbre[j]-1])
	elif nbre[j]==3:
		print("la personne a",valeur[nbre[j]-1],"ans")
	elif nbre[j]==4:
		if player[j]=='beaucoup':
			print("cette personne aime ",valeur[nbre[j]-1],"de personne")
		else:
			print("cette personne aime",valeur[nbre[j]-1])
	
	idea=input("alors est que tu a une idée de qui est cette elfe malicieux ?:")
	if idea == name:
		print("gg t'a fini mon petit jeu en",essai,'coup')
		break
	elif idea=="non":
		print('tu devrais pourtant sale merde')
		continue
	

	
	
	






