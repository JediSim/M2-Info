import csv
import numpy as np
from random import randint
from random import random
import matplotlib.pyplot as plt
import math

def extraire_sommets(fichier):
    """
    Extrait les sommets à partir d'un fichier CSV.
    :param fichier: Le fichier CSV contenant les sommets.
    :return: Un tableau contenant les sommets.
    """
    tab_tmp = []
    with open(fichier, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            tab_tmp.append(np.array(row, dtype=np.float64))
    return tab_tmp

def construire_matrice_distance(sommets):
    """
    Construit la matrice de distance à partir d'un fichier CSV.
    :param fichier: Le fichier CSV contenant les distances.
    :return: La matrice de distance.
    """
    matrice = np.zeros((250, 250), dtype=np.float64)
    
    for i in range(0, len(sommets)):
        for j in range(0, len(sommets)):
            matrice[i][j] = np.linalg.norm(sommets[i] - sommets[j])
            matrice[j][i] = matrice[i][j]

    matrice = np.array(matrice, dtype=np.float64)
    np.fill_diagonal(matrice, np.inf)

    return matrice

def get_distance(path, sommets):
    """
    Calcule la distance d'un chemin.
    :param path: Le chemin.
    :param sommets: Les sommets.
    :return: La distance du chemin.
    """
    distance = 0
    for i in range(0, len(path)-1):
        distance += np.linalg.norm(sommets[path[i]] - sommets[path[i+1]])
    distance += np.linalg.norm(sommets[path[0]] - sommets[path[len(path)-1]])
    return distance

def swap(sommets, i, j):
    """
    Échange deux sommets dans un tableau.
    :param sommets: Le tableau de sommets.
    :param i: L'indice du premier sommet.
    :param j: L'indice du deuxième sommet.
    """
    tmp = sommets[i]
    sommets[i] = sommets[j]
    sommets[j] = tmp
    return sommets

def swap_with_next(sommets, i):
    """
    Échange un sommet avec le suivant.
    :param sommets: Le tableau de sommets.
    :param i: L'indice du sommet à échanger.
    """
    if i+1 >= len(sommets):
        return swap(sommets, i, 0)
    return swap(sommets, i, i+1)

def insert_at(sommets, i, indice_ville):
    """
    Insère une ville à un indice donné.
    :param sommets: Le tableau de sommets.
    :param i: L'indice où insérer la ville.
    :param ville: l'indice de la ville à insérer.
    """
    tmp = sommets[indice_ville]
    sommets.remove(sommets[indice_ville])
    sommets.insert(i, indice_ville)
    return sommets

def do_2_opt(sommets, i, j):
    """
    Effectue un 2-opt sur un chemin.
    :param sommets: Le chemin.
    :param i: L'indice du premier sommet.
    :param j: L'indice du deuxième sommet.
    """
    if i > j:
        i, j = j+1, i-1
    tmp = sommets[i:j+1]
    tmp.reverse()
    sommets[i:j+1] = tmp
    return sommets

def voisin_random(sommets):
    a = randint(0, len(sommets)-1)
    b = randint(0, len(sommets)-1)
    transformation = randint(0, 3)

    # if transformation == 0:
    #     # return swap(sommets, a, b)
    #     return do_2_opt(sommets, a, b)
    # elif transformation == 1:
    #     # return swap_with_next(sommets, a)
    #     return do_2_opt(sommets, a, b)
    # elif transformation == 2:
    #     # return insert_at(sommets, a, b)
    #     return do_2_opt(sommets, a, b)
    # elif transformation == 3:
    #     return do_2_opt(sommets, a, b)
    return swap_with_next(sommets, a)

def plot_circuit(sommets, path):
    """
    Affiche le circuit.
    :param sommets: Les sommets.
    :param path: Le chemin.
    """
    plt.figure()
    for i in range(0, len(sommets)):
        plt.scatter(sommets[i][0], sommets[i][1])
    for i in range(0, len(path)-1):
        plt.plot((sommets[path[i]][0],sommets[path[i+1]][0]), (sommets[path[i]][1],sommets[path[i+1]][1]), 'r')
    plt.show()

def chemin_glouton(sommets, depart=0):
    """
    Calcule un chemin glouton.
    :param sommets: Les sommets.
    :return: Le chemin glouton.
    """
    path = []
    path.append(depart)
    sommets_visites = []
    sommets_visites.append(depart)
    while len(sommets_visites) != len(sommets):
        min = np.inf
        sommet_min = -1
        for i in range(0, len(sommets)):
            if i not in sommets_visites and matrice_distance[path[len(path)-1]][i] < min:
                min = matrice_distance[path[len(path)-1]][i]
                sommet_min = i
        path.append(sommet_min)
        sommets_visites.append(sommet_min)
    return path

def best_chemin_glouton(sommets):
    min_chemin = chemin_glouton(sommets, 0)
    min_distance = get_distance(min_chemin, sommets)
    for i in range(0, len(sommets)):
        chemin = chemin_glouton(sommets, i)
        distance = get_distance(chemin, sommets)
        if i == 0 or distance < min_distance:
            min_distance = distance
            min_chemin = chemin
    return min_chemin, min_distance

# Algorithme de recuit simulé
def recuit_simule(T0, L, alpha, K, sommets):
    # Initialisation
    T = T0
    x = chemin_glouton(sommets,247)
    F_x = get_distance(x, sommets)
    x_hat = x
    F_hat = F_x
    compteur = 0
    n = 0

    # Itération
    while compteur < K:
        y = voisin_random(x)  # Choix aléatoire dans le voisinage
        F_y = get_distance(y, sommets)
        delta_F = F_y - F_x

        if delta_F <= 0:
            
            x = y
            F_x = F_y
            if F_y < F_hat:
                x_hat = y
                F_hat = F_y
                compteur = 0  # On vient d'optimiser
            else:
                compteur += 1
        else:
            q = np.random.uniform(0, 1)
            if q <= math.exp(-delta_F / T):
                x = y
                F_x = F_y
            compteur += 1

        if n % L == 0:
            T *= alpha  # Refroidissement
        n += 1
    return x, F_x

sommets = extraire_sommets("defi250.csv")
matrice_distance = construire_matrice_distance(sommets)
print(matrice_distance)
path = [i for i in range(0, 250)]
distance = get_distance(path, sommets)
print(distance)
print("-----swap-----")
path = swap(path, 0, 1)
print(path)
print("-----swap_with_next-----")
path = swap_with_next(path, 0)
print(path)
print("-----insert_at-----")
path = insert_at(path, 0, 5)
print(path)
print("-----do_2_opt-----")
path = do_2_opt(path, 5, 10)
print(path)
test = [i for i in range(0, 5)]
print(test)
test = voisin_random(test)
print(test)

# chemin, distance = best_chemin_glouton(sommets)
# print(distance)
# print(chemin)
# plot_circuit(sommets, chemin)

chemin, distance = recuit_simule(10000, 5, 0.9, 50, sommets)
print(chemin)
print(len(chemin))
print(distance)
plot_circuit(sommets, chemin)
# chemin = chemin_glouton(sommets, 247)
# distance = get_distance(chemin, sommets)
# print(distance)
# plot_circuit(sommets, chemin)
