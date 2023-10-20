#!/usr/local/bin/python3

# -*- coding: utf-8 -*-
import sys
from math import sqrt





### -----------------------   Votre algorithme   ------------------------------

#  L'argument l contient une liste d'entiers de taille n

# Fonction fusionner(tableau gauche, tableau droit)
#     tableau résultat
#     Tant que gauche n'est pas vide et droit n'est pas vide
#         Si gauche[0] < droit[0]
#             Ajouter gauche[0] à résultat
#             Retirer le premier élément de gauche
#         Sinon
#             Ajouter droit[0] à résultat
#             Retirer le premier élément de droit
#     Fin Tant Que

#     Ajouter le reste de gauche à résultat
#     Ajouter le reste de droit à résultat
#     Retourner résultat

# Fonction triFusion(tableau)
#     Si la longueur du tableau est inférieure ou égale à 1
#         Retourner tableau
#     Sinon
#         Trouver le point médian du tableau
#         Diviser le tableau en deux moitiés, gauche et droit
#         gaucheTrié = triFusion(gauche)
#         droitTrié = triFusion(droit)
#         Retourner fusionner(gaucheTrié, droitTrié)
#     Fin Si

def fctNLogN(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        l1 = [x for x in l if x < pivot]
        l2 = [x for x in l if x > pivot]
        return fctNLogN(l1) + [pivot] + fctNLogN(l2)

def triCube(l):
    n = len(l)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if l[i] < l[j] and l[j] < l[k]:
                    l[i], l[k] = l[k], l[i]
    return l


def triInsertion(l):
    n = len(l)
    for i in range(1, n):
        elementCourant = l[i]
        j = i
        while j > 0 and l[j - 1] > elementCourant:
            l[j] = l[j - 1]
            j = j - 1
        l[j] = elementCourant
    return l

def fonctionN(l):
    res = 0 
    for i in range(0,len(l)):
        res += 1
    return res

def triExponentiel(tableau):
    res = 0
    for i in range(2**len(tableau)):
        res += 1


def fctAlgo( l ):
    '''
        À vous de jouer! 
    '''
    # fonctionN(l) # graphique 1
    # triInsertion(l) # graphique 2
    # triCube(l) # graphique 3
    # triExponentiel(l) # graphique 4
    fctNLogN(l) # graphique 5

    return 42 # En vrai, votre fonction n'a même pas besoin de retourner quelque chose 






### -----  Fonction mère (normalement il n'y a pas à modifier la suite)  ------

#  Aide indiquant comment utiliser notre fonction
def usage( nom ):
    print("Usage : " + nom + " file")
    print("  Importe un fichier file listant un ensemble d'entiers et")
    print("  applique votre algorithme sur cette liste d'entiers.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ce programme nécessite un fichier en argument.")
        usage(sys.argv[0])
        exit(1)

    verbose = True
    if len(sys.argv)>=3 and sys.argv[1] == "--mute":
        verbose = False
        filename = sys.argv[2]
    else:
        filename = sys.argv[1]

    tab = []
    file = open(filename, "r")
    try:
        next(file)
        for line in file:
            tab.append( int(line))
    finally:
        file.close()
    if verbose:
        print("Input: ")
        print(tab)

    val = fctAlgo(tab)

    if verbose:
        print("Output: ")
        print(val)
