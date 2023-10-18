#!/usr/local/bin/python3

import sys

# Fonction sommeMinRec( t, i )
#   Si i == 0 alors
#       retourne 0
#   Fin si
#   opt := +Infini
#   Pour x dans [ 1,3,5 ] faire
#       Si x <= i alors
#           tmp := t[i] + sommeMinRec( t, i-x )
#           Si tmp < opt alors
#               opt := tmp
#           Fin si
#       Fin si
#   Fin pour
#   retourne opt

def sommeMinRec( t, i ):
    if i == 0:
        return 0
    opt = float("inf")
    for x in [ 1,3,5 ]:
        if x <= i:
            tmp = t[i] + sommeMinRec( t, i-x )
            if tmp < opt:
                opt = tmp
    return opt

mem = {0: 0}
def sommeMinMemo(t, n):
    if n not in mem:
        for i in range(1, n + 1):
            opt = float('inf')
            for x in [1, 3, 5]:
                if x <= i:
                    tmp = t[i] + sommeMinMemo(t, i-x)
                    if tmp < opt:
                        opt = tmp
            mem[i] = opt
    return mem[n]


def usage( nom ):
    print("Usage : " + nom + " METHODE file")
    print("  Importe un fichier file decrivant la partie")
    print("  Valeurs valides pour METHODE :")
    print("  - sommeMin i -          i est la case a atteindre")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Ce programme nécessite une méthode et un fichier en arguments.")
        usage(sys.argv[0])
        exit(1)

    mute = 0

    if sys.argv[1] == "sommeMin":
        print("sommeMin")
        fct = sommeMinRec
    elif sys.argv[1] == "sommeMinMemo":
        fct = sommeMinMemo
    elif sys.argv[1] == "sommeMin_muette":
        fct = sommeMinRec
        mute = 1
    else:
        print("Cette méthode n'existe pas.")
        usage(sys.argv[0])
        exit(1)

    filename = sys.argv[2]
    tab = []
    file = open(filename, "r")
    try:
        next(file)
        for line in file:
            tab.append( int(line))
    finally:
        file.close()
    if mute == 0:
        print("input : ", end="")
        print(tab)

    # Si besoin, on peut augmenter le nombre de récursions possible pour les méthodes récursives
        #sys.setrecursionlimit(10 ** 6)
        #resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, -1))
    val = fct(tab, len(tab)-1)
    if mute == 0:
        print(val)