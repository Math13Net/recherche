
# PROBLEME DU SAC A DOS
# Problème: Un voleur possède un sac à dos pouvant contenir maximum 10kg et il a devant lui plsieurs objets de poids et de valeurs différentes.
# Quels objets le voleur devrait-il prendre pour repartir avec le plus d'argent dans son sac ?

# Les differents objets à voler:
noms=['A','B','C','D','E','F','G']
valeurs=[10,11,23,9,30,6,8]
masses=[2,4.5,5,4,9,1,2.5]

# Fonction qui crée un dictionnaire pour classer ces objets

def listeDictionnaires():
    '''Out: liste de dictionnaires dont les clés sont
            nom, valeur, masse et valeurMassique'''
    n=len(noms) # nb d'objets
    L=[]
    for i in range(n):
        d=dict()
        d['nom']= noms[i]
        d['valeur']= valeurs[i]
        d['masse']= masses[i]
        d['valeurMassique']= valeurs[i]/masses[i]
        L.append(d)
    L.sort(key=lambda d: d.get('valeurMassique'),reverse=True)
    return L

# Fonction qui calcule la valeur de la combinaison choisie

def  valeur(objets,masseMax):
    ''' In : une liste d'objets et un entier masseMax
        Out: valeur totale des objets de la liste objets
             si la masse des objets ne dépasse pas masseMax
             -1 sinon'''
    valeur=0
    masse=0
    for x in objets:
        i=noms.index(x) # indice de l'objet x
        valeur= valeur + valeurs[i] 
        masse= masse + masses[i]
    if masse<=masseMax:
        return valeur
    else:
        return -1 

# Fonction principale qui calcule une solution a peu près optimale
        
def sacAdosGlouton(masseMax):
    ''' In : un entier masseMax
        Out: la liste des objets renvoyée par l'algo glouton'''
    n=len(masses) # nb d'objets
    L=listeDictionnaires()
    masseDuSac=0
    objetsAprendre=[]
    i=0
    while masseDuSac+L[i]['masse']<=masseMax:
        objetsAprendre.append(L[i]['nom'])
        masseDuSac= masseDuSac + L[i]['masse']
        i= i + 1
    return objetsAprendre