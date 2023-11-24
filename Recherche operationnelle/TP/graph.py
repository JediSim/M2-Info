import numpy as np

class Graph:
    def __init__(self):
        self.sommets = []
        self.matriceAdjacence = []

    def addSommet(self, sommet):
        self.sommets.append(sommet)

    def addArc(self, sommet1, sommet2):
        sommet1.addVoisin(sommet2)

    def addArcDoubleSense(self, sommet1, sommet2):
        self.addArc(sommet1, sommet2)
        self.addArc(sommet2, sommet1)

    def getSommet(self, nom):
        for sommet in self.sommets:
            if sommet.nom == nom:
                return sommet
        return None
    
    def getVoisins(self, sommet):
        return sommet.voisin

    def getMatriceAdjacence(self):
        return self.matriceAdjacence

    def calcMatriceAdjacence(self):
        matrice = []
        for i in range(0, len(self.sommets)):
            matrice.append([])
            for j in range(0, len(self.sommets)):
                matrice[i].append(0)
            for k in range(0, len(self.sommets[i].voisin)):
                matrice[i][(self.sommets[i].voisin[k].nom)-1] = 1
        self.matriceAdjacence = np.array(matrice)

    def getDegreSortant(self, sommet):
        return len(sommet.voisin)

    def getDegreEntrant(self, sommet):
        return np.sum(axis=0, a=self.matriceAdjacence)[sommet.nom-1]

    def getSommetDistanceN(self, n):
        if len(self.matriceAdjacence) == len(self.sommets):
            self.calcMatriceAdjacence()
        matrice = self.matriceAdjacence
        for i in range(1, n):
            matrice = np.dot(matrice, self.matriceAdjacence)
        res = []
        for i in range(0, len(matrice)):
            for j in range(0, len(matrice[i])):
                if matrice[i][j] > 0:
                    res.append([self.sommets[i], self.sommets[j]])
        return res

    def getDistanceMin(self, sommet1, sommet2):
        if len(self.matriceAdjacence) == len(self.sommets):
            self.calcMatriceAdjacence()
        matrice = self.matriceAdjacence
        res = 1
        while matrice[sommet1.nom-1][sommet2.nom-1] == 0 or res > len(self.sommets):
            matrice = np.dot(matrice, self.matriceAdjacence)
            res += 1
        if res > len(self.sommets):
            return -1
        return res

    def __str__(self):
        res = "Graph:\n"
        self.calcMatriceAdjacence()
        for i in range(0, len(self.sommets)):
            sommet = self.sommets[i]
            res += str(sommet) + " degre entrant/sortant de " + str(i) + " : " + str(self.getDegreEntrant(sommet)) + "," + str(self.getDegreSortant(sommet)) + "\n"
        return res
    
class Sommet:
    def __init__(self, nom):
        self.nom = nom
        self.voisin = []

    def addVoisin(self, voisin):
        if voisin not in self.voisin:
            self.voisin.append(voisin)

    def __str__(self):
        return "Sommet: " + str(self.nom) + " Voisins: " + str(self.voisin)

    def __repr__(self):
        return str(self.nom)

    def __eq__(self, other):
        return self.nom == other.nom

    def __hash__(self):
        return hash(self.nom)


